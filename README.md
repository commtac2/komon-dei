# Komon DEI

Gentoo Repo for Komon Deus Ex Machinas by Komon Studios.
Just Sane Defaults.

Stay Tuned to https://komon.studio 

Associated Installation Guide: https://github.com/commtac2/Manny-Manuals/blob/bass/dxm-from-scratch-guide/0-dxm-introduction-hello.md

## AutoExpanding Image
Don't Exactly know Where to Host This, But Here's an AutoExpanding Image. 
AutoExpansion Worked For Me. YMMV. 

Download Link is Available Through Here:

```
https://komon.studio/komon-dei/introduction
```

The SHA Should Be,

```
7b641a430b827ee36842b82cfed39fde8404339eeac229e8ca8fc46d0621d7f2
```

The Username is `manny`, and the Answer to every Password is `hello`.

## What is DxM?

Deus Ex Machina (DxM) is a Little Gentoo Linux Based Operating System I Created Provided by the Komon Dei Repository.
It's not much, But I think there is a lot of room to grow with this as a template.

## What is Komon DEI

The Komon Dei repository is a Gentoo Ebuild Repository defining the Operating System's set of System Packages,
and Compilation Options for said packages.
Komon DEI offers several installation profiles including `dxm`, and `qxm-home`.
These profiles define what I hope are a good set of Packages, and Development Tools in a safe and secure manner.
Just a safe place to code, be online, and communicate.

## Selling Points

### Built with Free and Open Source Software

* This is Nice Because It Means We Do Not Have to Pay Them.

### Based on Hardened Gentoo Profiles

* The DEI profiles offered are derived from hardened parent profiles and are therefore hardened as well.
* Hardened Gentoo Profiles turn on a number of compilation, and toolchain options 
that make the system being built more secure.

### Hardened Kernel

* Just Because The Profile is Hardened Doesn't Mean The Seed Is.
* A Hardened Kernel Configuration offering sane defaults is included in the Komon Dei repository.
* Check out the Colonel's Recipe for more information.

### Encrypted Root

* Nowadays, I kinda wanna encrypt everything I can.
* DEI machines as described herein provide an encrypted root partition via LUKS encryption.
  * LUKS Spcification Here: (https://gitlab.com/cryptsetup/-/wikis/LUKS-standard/on-disk-format.pdf)
* Everything you're probably ever going to save on this computer will be encrypted with your choice of Symmetric Cipher
  such as AES or Serpent.
* Have that Family Recipe you never want getting out? 
  * save it on A Deus Ex Machina
  * keep it unplugged from internet if you really wanna make sure
  * Bam Bam
  * It's Quantum Resistantly Encrypted with your favorite cipher
* Like A Room of One's Own.

### Optimized For the Raspberry PI 5 Architecture

* Gentoo is Unique in that it allow us to compile all our programs from Scratch.
* Installed Programs are Especially Cooked for the onboard Cortex a76.
  * Compilation options include
    * Speculation barriers enabled on GCC
      * Sure. This will cost us some decent performance penalty. But, it hardens us against Spectre-Like Attacks.
    * Link Time Optimization
      * Sure. This makes Compilation Longer. But the Compilation time will more than pay for itself down the line.
    * Prediction Resistance Enabled on GCC
       * Sure. This costs us some performance on affected code paths. But, it hardens us against Spectre-Like Attacks.

### Good Base of System Packages

* Komon DEI offers a Good Starting Point For Development.
  * Comes with Development Tools, and Languages I (Me, Manny, Emanuel) Personally use Built In.
  * Includes,
    * Python (GIL and Python 3.13 Free Threading)
    * Rust
    * Go
    * Node (Select Profiles)
    * Docker (Select Profiles)
* Offers Commonly used Everyday Applications like 
  * FireFox
  * LibreOffice
  * Codium
  * SuperTux

### Common Sense USE Flags

* Komon Dei Profiles offer what I believe are Komon Sense USE flags offering a decent set of Compilation Defaults
for the architecture.

### Included Miscellaneous Files

* Includes what I believe are common sense Miscellaneous Configuration Files such as a Firewall (BigIron).
* Eases the Installation Process.

### Out Of the Box USB Smarcard support

* Out Of the Box SmartCard Support (FIDO, GPG, etc).
* Yubikey Manager preinstalled for Yubikey Configuration.

### Potential for Expansion

* There is A lot of Space for Improvement Here.
* I wanted to spend more time on this, but the World needs *something*


## Why Gentoo

* A Gentoo Penguin is the world's fastest penguin.
* The species calls in a variety of ways, but the most frequently heard is Allowed trumpeting,
  which the bird emits with its head thrown back.
* As the Gentoo waddles along on land, its tail sticks out behind, sweeping from side to side.
  * Hence the scientific name Pygoscelis, which means "rump-tailed".
* Nests are usually made from a roughly circular pile of stones.
  * The stones are jealously guarded.
  * They are also prized by females, As A male penguin can obtain favors by offering choice stones.

As of 2025, the Conservation Status of Gentoo Birds is listed as,

> Least Concern

## What Makes Gentoo Suitable

* A lot of the Power in Gentoo lies in its Package Manager: Portage
  * Most Linux Distributions offer PreBuilt Binaries for Packages (ArchLinux, Fedora, RedHat, Ubuntu, Debian, etc).
  * Gentoo and Portage allows program compilation according to the user's preferences via USE Flags. 
    * Allows For Optimization for the hardware on which it is installed.
* The Komon DEI is highly optimized for the Raspberry PI 5 Hardware in order to maximize performance, and security.

### Who uses Gentoo?

Portage is used by Google to build their Chromium OS.

Now I imagine they have their own private internal repositories with their own selection of 
  * Ebuilds
  * Tests and Balances
  * CVE/FEDRAMP Checks
  * And All That.

We Do Not Have All That.

By Creating a Deus Ex Machina Explicit trust is placed on the Open Source Community.
Now there are again checks and balances in place but the Open Source Community is also,

* tired
* under/not paid 
* lazy

So GodSpeed to us.

## Primer On Raspberry PI 5 Hardware

Some Facts:

* The Raspberry PI 5 uses a Broadcom BCM2712 application processor which includes a quad-core 
  Arm Cortex-A76 CPU Cluster running ARM v8.2a.
* Newer Models of the Raspberry PI 5 use the BCM2712D0 variation (or stepping) of the BCM2712 chip, 
  which has a little more free silicon space on the chip for activities.
* The Raspberry PI 5 uses a VideoCore VII GPU which utilizes the V3D device driver.

For our purposes this is all we really need to know.

All in All, the processing power on the Raspberry PI 5 is really weak relative to modern commercial computers.
It's kinda great this thing can run anything at all.

### Why Deus Ex Machina? Why DEI?

It was the name of a character from a show.
DEI is the plural of Deus. 
No religious/political affiliation whatsoever. Orthoginal to it.
Deuces to Deuses.

### What To Do If You Mess Up

Don't.

