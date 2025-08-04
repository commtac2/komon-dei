# Copyright 1999-2025 Gentoo Authors
# Distributed under the terms of the GNU General Public License v2

EAPI=8

ETYPE=sources
K_DEFCONFIG="bcm2712_defconfig"
K_SECURITY_UNSUPPORTED=1
EXTRAVERSION="-${PN}/-*"

K_EXP_GENPATCHES_NOUSE=1
K_GENPATCHES_VER=35
K_DEBLOB_AVAILABLE=0
K_WANT_GENPATCHES="base extras"

inherit kernel-2 linux-info
detect_version
detect_arch

#MY_P=$(ver_cut 4-)
#MY_P="stable_${MY_P/p/}"
COMMIT=23e6672404e861634632f17e9d3253d265cc8186
MY_P=${COMMIT}

DESCRIPTION="Raspberry PI Sources"
HOMEPAGE="https://github.com/raspberrypi/linux"
SRC_URI="
	https://github.com/raspberrypi/linux/archive/${MY_P}.tar.gz -> linux-${KV_FULL}.tar.gz
	${GENPATCHES_URI}
"

KEYWORDS="~arm64"

UNIPATCH_EXCLUDE="
	10*
	15*
	1700
	1730
    1740
	2000
    29*
	3000
    4567"

pkg_setup() {
	ewarn ""
	ewarn "${PN} is *not* supported by the Gentoo Kernel Project in any way."
	ewarn "If you need support, please contact your Mother."
	ewarn "Do *not* open bugs in Gentoo's bugzilla unless you have issues with"
	ewarn "the ebuilds. Thank you."
	ewarn "You Are Welcome."
	ewarn ""

	kernel-2_pkg_setup
}

universal_unpack() {
	unpack linux-${KV_FULL}.tar.gz

	# We want to rename the unpacked directory to a nice normalised string
	# bug #762766
	mv "${WORKDIR}"/linux-${MY_P} "${WORKDIR}"/linux-${KV_FULL} || die

	# remove all backup files
	find . -iname "*~" -exec rm {} \; 2>/dev/null
}

src_prepare() {
	default
	kernel-2_src_prepare
}

pkg_postinst() {
	kernel-2_pkg_postinst
}

pkg_postrm() {
	kernel-2_pkg_postrm
}

