#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kio-extras
Version  : 20.04.0
Release  : 40
URL      : https://download.kde.org/stable/release-service/20.04.0/src/kio-extras-20.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.04.0/src/kio-extras-20.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.04.0/src/kio-extras-20.04.0.tar.xz.sig
Summary  : Additional components to increase the functionality of KIO
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 MIT
Requires: kio-extras-data = %{version}-%{release}
Requires: kio-extras-lib = %{version}-%{release}
Requires: kio-extras-license = %{version}-%{release}
Requires: kio-extras-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules gperf
BuildRequires : extra-cmake-modules pkgconfig(OpenEXR)
BuildRequires : kdnssd-dev
BuildRequires : kdsoap-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libssh-dev
BuildRequires : phonon-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libmtp)
BuildRequires : pkgconfig(libtirpc)
BuildRequires : pkgconfig(smbclient)
BuildRequires : qtbase-dev mesa-dev
BuildRequires : syntax-highlighting-dev
BuildRequires : taglib-dev

%description
Overview of kio_fish
====================
FISH is a protocol to get filesystem access without special server
software, only using a remote shell. (Hence the name: FIles transferred
over SHell protocol).
It was first devised by Pavel Machek <pavel@bug.ucw.cz> and implemented
as a Midnight Commander vfs module in 1998.

%package data
Summary: data components for the kio-extras package.
Group: Data

%description data
data components for the kio-extras package.


%package dev
Summary: dev components for the kio-extras package.
Group: Development
Requires: kio-extras-lib = %{version}-%{release}
Requires: kio-extras-data = %{version}-%{release}
Provides: kio-extras-devel = %{version}-%{release}
Requires: kio-extras = %{version}-%{release}
Requires: kio-extras = %{version}-%{release}

%description dev
dev components for the kio-extras package.


%package doc
Summary: doc components for the kio-extras package.
Group: Documentation

%description doc
doc components for the kio-extras package.


%package lib
Summary: lib components for the kio-extras package.
Group: Libraries
Requires: kio-extras-data = %{version}-%{release}
Requires: kio-extras-license = %{version}-%{release}

%description lib
lib components for the kio-extras package.


%package license
Summary: license components for the kio-extras package.
Group: Default

%description license
license components for the kio-extras package.


%package locales
Summary: locales components for the kio-extras package.
Group: Default

%description locales
locales components for the kio-extras package.


%prep
%setup -q -n kio-extras-20.04.0
cd %{_builddir}/kio-extras-20.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587738516
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DLIBSSH_LIBRARIES="-lssh"
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1587738516
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kio-extras
cp %{_builddir}/kio-extras-20.04.0/COPYING.GPLv2 %{buildroot}/usr/share/package-licenses/kio-extras/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/kio-extras-20.04.0/COPYING.LGPLv2.0 %{buildroot}/usr/share/package-licenses/kio-extras/ba8966e2473a9969bdcab3dc82274c817cfd98a1
cp %{_builddir}/kio-extras-20.04.0/COPYING.LGPLv2.1 %{buildroot}/usr/share/package-licenses/kio-extras/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/kio-extras-20.04.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kio-extras/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kio-extras-20.04.0/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/kio-extras/ff3ed70db4739b3c6747c7f624fe2bad70802987
cp %{_builddir}/kio-extras-20.04.0/fish/COPYING %{buildroot}/usr/share/package-licenses/kio-extras/6faad2cf3a1ae0af81ae8c58563712e95d36237a
cp %{_builddir}/kio-extras-20.04.0/info/LICENSE %{buildroot}/usr/share/package-licenses/kio-extras/3e6eb4f637da85026b5720924da3536b84cb339e
cp %{_builddir}/kio-extras-20.04.0/man/LICENSE %{buildroot}/usr/share/package-licenses/kio-extras/67218f86a21c5afe177def300337c7ff8ccf40f9
cp %{_builddir}/kio-extras-20.04.0/mtp/COPYING %{buildroot}/usr/share/package-licenses/kio-extras/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/kio-extras-20.04.0/mtp/LICENCE %{buildroot}/usr/share/package-licenses/kio-extras/4cc77b90af91e615a64ae04893fdffa7939db84c
pushd clr-build
%make_install
popd
%find_lang kfileaudiopreview5
%find_lang kio5_activities
%find_lang kio5_archive
%find_lang kio5_bookmarks
%find_lang kio5_fish
%find_lang kio5_info
%find_lang kio5_man
%find_lang kio5_mtp
%find_lang kio5_nfs
%find_lang kio5_recentdocuments
%find_lang kio5_sftp
%find_lang kio5_smb
%find_lang kio5_thumbnail
%find_lang kio5_network

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/config.kcfg/jpegcreatorsettings5.kcfg
/usr/share/dbus-1/interfaces/kf5_org.kde.network.kioslavenotifier.xml
/usr/share/dbus-1/services/org.kde.kmtp.daemon.service
/usr/share/kio_bookmarks/kio_bookmarks.css
/usr/share/kio_docfilter/kio_docfilter.css
/usr/share/kio_info/kde-info2html
/usr/share/kio_info/kde-info2html.conf
/usr/share/konqsidebartng/virtual_folders/remote/virtualfolder_network.desktop
/usr/share/konqueror/dirtree/remote/mtp-network.desktop
/usr/share/konqueror/dirtree/remote/smb-network.desktop
/usr/share/kservices5/about.protocol
/usr/share/kservices5/ar.protocol
/usr/share/kservices5/audiothumbnail.desktop
/usr/share/kservices5/bookmarks.protocol
/usr/share/kservices5/bzip.protocol
/usr/share/kservices5/bzip2.protocol
/usr/share/kservices5/comicbookthumbnail.desktop
/usr/share/kservices5/cursorthumbnail.desktop
/usr/share/kservices5/directorythumbnail.desktop
/usr/share/kservices5/djvuthumbnail.desktop
/usr/share/kservices5/ebookthumbnail.desktop
/usr/share/kservices5/exrthumbnail.desktop
/usr/share/kservices5/filenamesearch.protocol
/usr/share/kservices5/fish.protocol
/usr/share/kservices5/gzip.protocol
/usr/share/kservices5/imagethumbnail.desktop
/usr/share/kservices5/info.protocol
/usr/share/kservices5/jpegthumbnail.desktop
/usr/share/kservices5/kraorathumbnail.desktop
/usr/share/kservices5/lzma.protocol
/usr/share/kservices5/man.protocol
/usr/share/kservices5/mtp.protocol
/usr/share/kservices5/network.protocol
/usr/share/kservices5/nfs.protocol
/usr/share/kservices5/opendocumentthumbnail.desktop
/usr/share/kservices5/recentdocuments.protocol
/usr/share/kservices5/settings.protocol
/usr/share/kservices5/sevenz.protocol
/usr/share/kservices5/sftp.protocol
/usr/share/kservices5/svgthumbnail.desktop
/usr/share/kservices5/tar.protocol
/usr/share/kservices5/textthumbnail.desktop
/usr/share/kservices5/thumbnail.protocol
/usr/share/kservices5/windowsexethumbnail.desktop
/usr/share/kservices5/windowsimagethumbnail.desktop
/usr/share/kservices5/xz.protocol
/usr/share/kservices5/zip.protocol
/usr/share/kservicetypes5/thumbcreator.desktop
/usr/share/mime-packages/kf5_network.xml
/usr/share/qlogging-categories5/kio-extras.categories
/usr/share/remoteview/mtp-network.desktop
/usr/share/remoteview/network.desktop
/usr/share/remoteview/smb-network.desktop
/usr/share/solid/actions/solid_mtp.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/kio_archivebase.h
/usr/include/KF5/libkioarchive_export.h
/usr/lib64/cmake/KioArchive/KioArchiveConfig.cmake
/usr/lib64/cmake/KioArchive/KioArchiveConfigVersion.cmake
/usr/lib64/cmake/KioArchive/KioArchiveTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KioArchive/KioArchiveTargets.cmake

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kioslave5/bookmarks/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/bookmarks/index.docbook
/usr/share/doc/HTML/ca/kioslave5/bzip2/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/bzip2/index.docbook
/usr/share/doc/HTML/ca/kioslave5/fish/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/fish/index.docbook
/usr/share/doc/HTML/ca/kioslave5/gzip/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/gzip/index.docbook
/usr/share/doc/HTML/ca/kioslave5/info/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/info/index.docbook
/usr/share/doc/HTML/ca/kioslave5/man/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/man/index.docbook
/usr/share/doc/HTML/ca/kioslave5/network/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/network/index.docbook
/usr/share/doc/HTML/ca/kioslave5/nfs/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/nfs/index.docbook
/usr/share/doc/HTML/ca/kioslave5/recentdocuments/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/recentdocuments/index.docbook
/usr/share/doc/HTML/ca/kioslave5/sftp/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/sftp/index.docbook
/usr/share/doc/HTML/ca/kioslave5/smb/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/smb/index.docbook
/usr/share/doc/HTML/ca/kioslave5/tar/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/tar/index.docbook
/usr/share/doc/HTML/ca/kioslave5/thumbnail/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/thumbnail/index.docbook
/usr/share/doc/HTML/ca/kioslave5/xz/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/xz/index.docbook
/usr/share/doc/HTML/de/kioslave5/bookmarks/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/bookmarks/index.docbook
/usr/share/doc/HTML/de/kioslave5/bzip2/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/bzip2/index.docbook
/usr/share/doc/HTML/de/kioslave5/fish/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/fish/index.docbook
/usr/share/doc/HTML/de/kioslave5/gzip/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/gzip/index.docbook
/usr/share/doc/HTML/de/kioslave5/info/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/info/index.docbook
/usr/share/doc/HTML/de/kioslave5/man/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/man/index.docbook
/usr/share/doc/HTML/de/kioslave5/network/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/network/index.docbook
/usr/share/doc/HTML/de/kioslave5/nfs/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/nfs/index.docbook
/usr/share/doc/HTML/de/kioslave5/recentdocuments/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/recentdocuments/index.docbook
/usr/share/doc/HTML/de/kioslave5/sftp/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/sftp/index.docbook
/usr/share/doc/HTML/de/kioslave5/smb/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/smb/index.docbook
/usr/share/doc/HTML/de/kioslave5/tar/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/tar/index.docbook
/usr/share/doc/HTML/de/kioslave5/thumbnail/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/thumbnail/index.docbook
/usr/share/doc/HTML/de/kioslave5/xz/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/xz/index.docbook
/usr/share/doc/HTML/en/kioslave5/bookmarks/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/bookmarks/index.docbook
/usr/share/doc/HTML/en/kioslave5/bzip2/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/bzip2/index.docbook
/usr/share/doc/HTML/en/kioslave5/fish/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/fish/index.docbook
/usr/share/doc/HTML/en/kioslave5/gzip/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/gzip/index.docbook
/usr/share/doc/HTML/en/kioslave5/info/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/info/index.docbook
/usr/share/doc/HTML/en/kioslave5/man/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/man/index.docbook
/usr/share/doc/HTML/en/kioslave5/network/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/network/index.docbook
/usr/share/doc/HTML/en/kioslave5/nfs/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/nfs/index.docbook
/usr/share/doc/HTML/en/kioslave5/recentdocuments/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/recentdocuments/index.docbook
/usr/share/doc/HTML/en/kioslave5/sftp/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/sftp/index.docbook
/usr/share/doc/HTML/en/kioslave5/smb/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/smb/index.docbook
/usr/share/doc/HTML/en/kioslave5/tar/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/tar/index.docbook
/usr/share/doc/HTML/en/kioslave5/thumbnail/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/thumbnail/index.docbook
/usr/share/doc/HTML/en/kioslave5/xz/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/xz/index.docbook
/usr/share/doc/HTML/es/kioslave5/bookmarks/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/bookmarks/index.docbook
/usr/share/doc/HTML/es/kioslave5/bzip2/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/bzip2/index.docbook
/usr/share/doc/HTML/es/kioslave5/fish/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/fish/index.docbook
/usr/share/doc/HTML/es/kioslave5/gzip/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/gzip/index.docbook
/usr/share/doc/HTML/es/kioslave5/info/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/info/index.docbook
/usr/share/doc/HTML/es/kioslave5/man/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/man/index.docbook
/usr/share/doc/HTML/es/kioslave5/network/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/network/index.docbook
/usr/share/doc/HTML/es/kioslave5/nfs/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/nfs/index.docbook
/usr/share/doc/HTML/es/kioslave5/sftp/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/sftp/index.docbook
/usr/share/doc/HTML/es/kioslave5/smb/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/smb/index.docbook
/usr/share/doc/HTML/es/kioslave5/tar/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/tar/index.docbook
/usr/share/doc/HTML/es/kioslave5/thumbnail/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/thumbnail/index.docbook
/usr/share/doc/HTML/es/kioslave5/xz/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/xz/index.docbook
/usr/share/doc/HTML/et/kioslave5/bookmarks/index.cache.bz2
/usr/share/doc/HTML/et/kioslave5/bookmarks/index.docbook
/usr/share/doc/HTML/et/kioslave5/bzip2/index.cache.bz2
/usr/share/doc/HTML/et/kioslave5/bzip2/index.docbook
/usr/share/doc/HTML/et/kioslave5/fish/index.cache.bz2
/usr/share/doc/HTML/et/kioslave5/fish/index.docbook
/usr/share/doc/HTML/et/kioslave5/gzip/index.cache.bz2
/usr/share/doc/HTML/et/kioslave5/gzip/index.docbook
/usr/share/doc/HTML/et/kioslave5/info/index.cache.bz2
/usr/share/doc/HTML/et/kioslave5/info/index.docbook
/usr/share/doc/HTML/et/kioslave5/man/index.cache.bz2
/usr/share/doc/HTML/et/kioslave5/man/index.docbook
/usr/share/doc/HTML/et/kioslave5/network/index.cache.bz2
/usr/share/doc/HTML/et/kioslave5/network/index.docbook
/usr/share/doc/HTML/et/kioslave5/nfs/index.cache.bz2
/usr/share/doc/HTML/et/kioslave5/nfs/index.docbook
/usr/share/doc/HTML/et/kioslave5/sftp/index.cache.bz2
/usr/share/doc/HTML/et/kioslave5/sftp/index.docbook
/usr/share/doc/HTML/et/kioslave5/smb/index.cache.bz2
/usr/share/doc/HTML/et/kioslave5/smb/index.docbook
/usr/share/doc/HTML/et/kioslave5/tar/index.cache.bz2
/usr/share/doc/HTML/et/kioslave5/tar/index.docbook
/usr/share/doc/HTML/et/kioslave5/thumbnail/index.cache.bz2
/usr/share/doc/HTML/et/kioslave5/thumbnail/index.docbook
/usr/share/doc/HTML/et/kioslave5/xz/index.cache.bz2
/usr/share/doc/HTML/et/kioslave5/xz/index.docbook
/usr/share/doc/HTML/it/kioslave5/bookmarks/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/bookmarks/index.docbook
/usr/share/doc/HTML/it/kioslave5/bzip2/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/bzip2/index.docbook
/usr/share/doc/HTML/it/kioslave5/fish/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/fish/index.docbook
/usr/share/doc/HTML/it/kioslave5/gzip/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/gzip/index.docbook
/usr/share/doc/HTML/it/kioslave5/info/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/info/index.docbook
/usr/share/doc/HTML/it/kioslave5/man/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/man/index.docbook
/usr/share/doc/HTML/it/kioslave5/network/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/network/index.docbook
/usr/share/doc/HTML/it/kioslave5/nfs/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/nfs/index.docbook
/usr/share/doc/HTML/it/kioslave5/recentdocuments/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/recentdocuments/index.docbook
/usr/share/doc/HTML/it/kioslave5/sftp/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/sftp/index.docbook
/usr/share/doc/HTML/it/kioslave5/smb/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/smb/index.docbook
/usr/share/doc/HTML/it/kioslave5/tar/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/tar/index.docbook
/usr/share/doc/HTML/it/kioslave5/thumbnail/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/thumbnail/index.docbook
/usr/share/doc/HTML/it/kioslave5/xz/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/xz/index.docbook
/usr/share/doc/HTML/nb/kioslave5/man/index.cache.bz2
/usr/share/doc/HTML/nb/kioslave5/man/index.docbook
/usr/share/doc/HTML/nb/kioslave5/thumbnail/index.cache.bz2
/usr/share/doc/HTML/nb/kioslave5/thumbnail/index.docbook
/usr/share/doc/HTML/nl/kioslave5/bookmarks/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/bookmarks/index.docbook
/usr/share/doc/HTML/nl/kioslave5/bzip2/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/bzip2/index.docbook
/usr/share/doc/HTML/nl/kioslave5/fish/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/fish/index.docbook
/usr/share/doc/HTML/nl/kioslave5/gzip/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/gzip/index.docbook
/usr/share/doc/HTML/nl/kioslave5/info/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/info/index.docbook
/usr/share/doc/HTML/nl/kioslave5/man/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/man/index.docbook
/usr/share/doc/HTML/nl/kioslave5/network/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/network/index.docbook
/usr/share/doc/HTML/nl/kioslave5/nfs/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/nfs/index.docbook
/usr/share/doc/HTML/nl/kioslave5/recentdocuments/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/recentdocuments/index.docbook
/usr/share/doc/HTML/nl/kioslave5/sftp/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/sftp/index.docbook
/usr/share/doc/HTML/nl/kioslave5/smb/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/smb/index.docbook
/usr/share/doc/HTML/nl/kioslave5/tar/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/tar/index.docbook
/usr/share/doc/HTML/nl/kioslave5/thumbnail/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/thumbnail/index.docbook
/usr/share/doc/HTML/nl/kioslave5/xz/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/xz/index.docbook
/usr/share/doc/HTML/pt/kioslave5/bookmarks/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/bookmarks/index.docbook
/usr/share/doc/HTML/pt/kioslave5/bzip2/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/bzip2/index.docbook
/usr/share/doc/HTML/pt/kioslave5/fish/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/fish/index.docbook
/usr/share/doc/HTML/pt/kioslave5/gzip/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/gzip/index.docbook
/usr/share/doc/HTML/pt/kioslave5/info/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/info/index.docbook
/usr/share/doc/HTML/pt/kioslave5/man/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/man/index.docbook
/usr/share/doc/HTML/pt/kioslave5/network/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/network/index.docbook
/usr/share/doc/HTML/pt/kioslave5/nfs/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/nfs/index.docbook
/usr/share/doc/HTML/pt/kioslave5/recentdocuments/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/recentdocuments/index.docbook
/usr/share/doc/HTML/pt/kioslave5/sftp/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/sftp/index.docbook
/usr/share/doc/HTML/pt/kioslave5/smb/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/smb/index.docbook
/usr/share/doc/HTML/pt/kioslave5/tar/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/tar/index.docbook
/usr/share/doc/HTML/pt/kioslave5/thumbnail/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/thumbnail/index.docbook
/usr/share/doc/HTML/pt/kioslave5/xz/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/xz/index.docbook
/usr/share/doc/HTML/pt_BR/kioslave5/bookmarks/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioslave5/bookmarks/index.docbook
/usr/share/doc/HTML/pt_BR/kioslave5/bzip2/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioslave5/bzip2/index.docbook
/usr/share/doc/HTML/pt_BR/kioslave5/fish/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioslave5/fish/index.docbook
/usr/share/doc/HTML/pt_BR/kioslave5/gzip/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioslave5/gzip/index.docbook
/usr/share/doc/HTML/pt_BR/kioslave5/info/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioslave5/info/index.docbook
/usr/share/doc/HTML/pt_BR/kioslave5/man/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioslave5/man/index.docbook
/usr/share/doc/HTML/pt_BR/kioslave5/network/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioslave5/network/index.docbook
/usr/share/doc/HTML/pt_BR/kioslave5/nfs/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioslave5/nfs/index.docbook
/usr/share/doc/HTML/pt_BR/kioslave5/sftp/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioslave5/sftp/index.docbook
/usr/share/doc/HTML/pt_BR/kioslave5/smb/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioslave5/smb/index.docbook
/usr/share/doc/HTML/pt_BR/kioslave5/tar/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioslave5/tar/index.docbook
/usr/share/doc/HTML/pt_BR/kioslave5/thumbnail/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioslave5/thumbnail/index.docbook
/usr/share/doc/HTML/pt_BR/kioslave5/xz/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioslave5/xz/index.docbook
/usr/share/doc/HTML/ru/kioslave5/gzip/index.cache.bz2
/usr/share/doc/HTML/ru/kioslave5/gzip/index.docbook
/usr/share/doc/HTML/ru/kioslave5/nfs/index.cache.bz2
/usr/share/doc/HTML/ru/kioslave5/nfs/index.docbook
/usr/share/doc/HTML/ru/kioslave5/sftp/index.cache.bz2
/usr/share/doc/HTML/ru/kioslave5/sftp/index.docbook
/usr/share/doc/HTML/ru/kioslave5/tar/index.cache.bz2
/usr/share/doc/HTML/ru/kioslave5/tar/index.docbook
/usr/share/doc/HTML/ru/kioslave5/thumbnail/index.cache.bz2
/usr/share/doc/HTML/ru/kioslave5/thumbnail/index.docbook
/usr/share/doc/HTML/sr/kioslave5/bookmarks/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/bookmarks/index.docbook
/usr/share/doc/HTML/sr/kioslave5/bzip2/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/bzip2/index.docbook
/usr/share/doc/HTML/sr/kioslave5/fish/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/fish/index.docbook
/usr/share/doc/HTML/sr/kioslave5/gzip/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/gzip/index.docbook
/usr/share/doc/HTML/sr/kioslave5/info/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/info/index.docbook
/usr/share/doc/HTML/sr/kioslave5/man/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/man/index.docbook
/usr/share/doc/HTML/sr/kioslave5/network/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/network/index.docbook
/usr/share/doc/HTML/sr/kioslave5/nfs/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/nfs/index.docbook
/usr/share/doc/HTML/sr/kioslave5/recentdocuments/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/recentdocuments/index.docbook
/usr/share/doc/HTML/sr/kioslave5/sftp/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/sftp/index.docbook
/usr/share/doc/HTML/sr/kioslave5/smb/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/smb/index.docbook
/usr/share/doc/HTML/sr/kioslave5/tar/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/tar/index.docbook
/usr/share/doc/HTML/sr/kioslave5/thumbnail/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/thumbnail/index.docbook
/usr/share/doc/HTML/sr/kioslave5/xz/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/xz/index.docbook
/usr/share/doc/HTML/sv/kioslave5/bookmarks/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/bookmarks/index.docbook
/usr/share/doc/HTML/sv/kioslave5/bzip2/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/bzip2/index.docbook
/usr/share/doc/HTML/sv/kioslave5/fish/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/fish/index.docbook
/usr/share/doc/HTML/sv/kioslave5/gzip/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/gzip/index.docbook
/usr/share/doc/HTML/sv/kioslave5/info/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/info/index.docbook
/usr/share/doc/HTML/sv/kioslave5/man/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/man/index.docbook
/usr/share/doc/HTML/sv/kioslave5/network/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/network/index.docbook
/usr/share/doc/HTML/sv/kioslave5/nfs/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/nfs/index.docbook
/usr/share/doc/HTML/sv/kioslave5/recentdocuments/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/recentdocuments/index.docbook
/usr/share/doc/HTML/sv/kioslave5/sftp/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/sftp/index.docbook
/usr/share/doc/HTML/sv/kioslave5/smb/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/smb/index.docbook
/usr/share/doc/HTML/sv/kioslave5/tar/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/tar/index.docbook
/usr/share/doc/HTML/sv/kioslave5/thumbnail/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/thumbnail/index.docbook
/usr/share/doc/HTML/sv/kioslave5/xz/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/xz/index.docbook
/usr/share/doc/HTML/uk/kioslave5/bookmarks/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/bookmarks/index.docbook
/usr/share/doc/HTML/uk/kioslave5/bzip2/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/bzip2/index.docbook
/usr/share/doc/HTML/uk/kioslave5/fish/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/fish/index.docbook
/usr/share/doc/HTML/uk/kioslave5/gzip/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/gzip/index.docbook
/usr/share/doc/HTML/uk/kioslave5/info/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/info/index.docbook
/usr/share/doc/HTML/uk/kioslave5/man/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/man/index.docbook
/usr/share/doc/HTML/uk/kioslave5/network/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/network/index.docbook
/usr/share/doc/HTML/uk/kioslave5/nfs/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/nfs/index.docbook
/usr/share/doc/HTML/uk/kioslave5/recentdocuments/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/recentdocuments/index.docbook
/usr/share/doc/HTML/uk/kioslave5/sftp/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/sftp/index.docbook
/usr/share/doc/HTML/uk/kioslave5/smb/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/smb/index.docbook
/usr/share/doc/HTML/uk/kioslave5/tar/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/tar/index.docbook
/usr/share/doc/HTML/uk/kioslave5/thumbnail/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/thumbnail/index.docbook
/usr/share/doc/HTML/uk/kioslave5/xz/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/xz/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkioarchive.so.5
/usr/lib64/libkioarchive.so.5.97.0
/usr/lib64/libmolletnetwork5.so.20
/usr/lib64/libmolletnetwork5.so.20.04.0
/usr/lib64/qt5/plugins/audiothumbnail.so
/usr/lib64/qt5/plugins/comicbookthumbnail.so
/usr/lib64/qt5/plugins/cursorthumbnail.so
/usr/lib64/qt5/plugins/djvuthumbnail.so
/usr/lib64/qt5/plugins/ebookthumbnail.so
/usr/lib64/qt5/plugins/exrthumbnail.so
/usr/lib64/qt5/plugins/imagethumbnail.so
/usr/lib64/qt5/plugins/jpegthumbnail.so
/usr/lib64/qt5/plugins/kf5/kded/filenamesearchmodule.so
/usr/lib64/qt5/plugins/kf5/kded/networkwatcher.so
/usr/lib64/qt5/plugins/kf5/kded/recentdocumentsnotifier.so
/usr/lib64/qt5/plugins/kf5/kio/about.so
/usr/lib64/qt5/plugins/kf5/kio/archive.so
/usr/lib64/qt5/plugins/kf5/kio/bookmarks.so
/usr/lib64/qt5/plugins/kf5/kio/filenamesearch.so
/usr/lib64/qt5/plugins/kf5/kio/filter.so
/usr/lib64/qt5/plugins/kf5/kio/fish.so
/usr/lib64/qt5/plugins/kf5/kio/info.so
/usr/lib64/qt5/plugins/kf5/kio/man.so
/usr/lib64/qt5/plugins/kf5/kio/mtp.so
/usr/lib64/qt5/plugins/kf5/kio/network.so
/usr/lib64/qt5/plugins/kf5/kio/nfs.so
/usr/lib64/qt5/plugins/kf5/kio/recentdocuments.so
/usr/lib64/qt5/plugins/kf5/kio/settings.so
/usr/lib64/qt5/plugins/kf5/kio/sftp.so
/usr/lib64/qt5/plugins/kf5/kio/smb.so
/usr/lib64/qt5/plugins/kf5/kio/thumbnail.so
/usr/lib64/qt5/plugins/kf5/kiod/kmtpd.so
/usr/lib64/qt5/plugins/kfileaudiopreview.so
/usr/lib64/qt5/plugins/kritathumbnail.so
/usr/lib64/qt5/plugins/opendocumentthumbnail.so
/usr/lib64/qt5/plugins/svgthumbnail.so
/usr/lib64/qt5/plugins/textthumbnail.so
/usr/lib64/qt5/plugins/windowsexethumbnail.so
/usr/lib64/qt5/plugins/windowsimagethumbnail.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kio-extras/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/kio-extras/3e6eb4f637da85026b5720924da3536b84cb339e
/usr/share/package-licenses/kio-extras/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kio-extras/67218f86a21c5afe177def300337c7ff8ccf40f9
/usr/share/package-licenses/kio-extras/6faad2cf3a1ae0af81ae8c58563712e95d36237a
/usr/share/package-licenses/kio-extras/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kio-extras/ba8966e2473a9969bdcab3dc82274c817cfd98a1
/usr/share/package-licenses/kio-extras/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files locales -f kfileaudiopreview5.lang -f kio5_activities.lang -f kio5_archive.lang -f kio5_bookmarks.lang -f kio5_fish.lang -f kio5_info.lang -f kio5_man.lang -f kio5_mtp.lang -f kio5_nfs.lang -f kio5_recentdocuments.lang -f kio5_sftp.lang -f kio5_smb.lang -f kio5_thumbnail.lang -f kio5_network.lang
%defattr(-,root,root,-)

