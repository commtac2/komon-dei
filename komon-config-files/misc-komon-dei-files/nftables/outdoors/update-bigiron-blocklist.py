#!/usr/bin/env python3

"""
Updates the nftables whitelist_v4 set with the latest blocklist from Proofpoint and Spamhaus.
Only does IPV4, until the day my ISP gives me an IPV6.
"""

import ipaddress
import json
import subprocess
from urllib.request import urlopen

TABLE_NAME = "bigiron"

# BlockList Feeds
PROOFPOINT_URLS = [
    "https://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt"
]
SPAMHAUS_URLS = [
    "https://www.spamhaus.org/drop/drop_v4.json",
]

PROOFPOINT_FEEDS = [ (feed_url, "#") for feed_url in PROOFPOINT_URLS]
SPAMHAUS_FEEDS = [(feed_url, None) for feed_url in SPAMHAUS_URLS]
ALL_FEEDS_FLAT = [*PROOFPOINT_FEEDS, *SPAMHAUS_FEEDS]

def fetch_feed(url, comment_prefix):
    """
    Yield CIDR strings from url

    * Text feeds (.txt)   → skip blank/comment lines (start with comment_prefix).
    * JSON feeds (.json)  → each line is a JSON object; emit its cidr field.
    """
    with urlopen(url, timeout=30) as resp:
        if url.endswith(".json"):
            for raw in resp:
                line = raw.decode().strip()
                if not line:
                    continue
                try:
                    cidr = json.loads(line)["cidr"]
                    if cidr:
                        yield cidr
                except (json.JSONDecodeError, KeyError):
                    continue
        else:
            for raw in resp:
                line = raw.decode().strip()
                if line and not line.startswith(comment_prefix or ""):
                    yield line


def numeric_key(net):
    """
    Sort key for interval sets: by integer address then prefix length.
    Guarantees strictly ascending order, as nftables requires.
    """
    return int(net.network_address), net.prefixlen


def reload_set(name: str, tablename: str, cidrs: list[str]):
    """Flush and Insert If Exists"""
    if cidrs:                                   # skip add element if list empty
        elems = ", ".join(cidrs)
        subprocess.run( ["nft", "flush", "set", "inet", tablename, name], check=True)
        subprocess.run( ["nft", "add", "element", "inet", tablename, name, "{", elems, "}"], check=True)

def main():
    seen: set[str] = set()
    v4: list[ipaddress.IPv4Network] = []

    # 1. collect + dedupe
    for url, comment in ALL_FEEDS_FLAT:
        for entry in fetch_feed(url, comment):
            if entry in seen:
                continue
            seen.add(entry)
            try:
                net = ipaddress.ip_network(entry, strict=False)
            except ValueError:
                continue
            (v6 if net.version == 6 else v4).append(net)

    # 2. sort for interval validation
    v4 = sorted(ipaddress.collapse_addresses(v4), key=numeric_key)

    # 3. Reload
    reload_set("whitelist_v4", TABLE_NAME, [str(n) for n in v4])

if __name__ == "__main__":
    main()

