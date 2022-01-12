#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kio-extras
Version  : 21.12.1
Release  : 62
URL      : https://download.kde.org/stable/release-service/21.12.1/src/kio-extras-21.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.12.1/src/kio-extras-21.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.12.1/src/kio-extras-21.12.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0 MIT
Requires: kio-extras-data = %{version}-%{release}
Requires: kio-extras-lib = %{version}-%{release}
Requires: kio-extras-license = %{version}-%{release}
Requires: kio-extras-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules gperf
BuildRequires : extra-cmake-modules pkgconfig(OpenEXR)
BuildRequires : extra-cmake-modules-data
BuildRequires : glibc-dev
BuildRequires : kactivities-dev
BuildRequires : kactivities-stats-dev
BuildRequires : kdnssd-dev
BuildRequires : kdsoap-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libssh-dev
BuildRequires : phonon-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libmtp)
BuildRequires : pkgconfig(libtirpc)
BuildRequires : pkgconfig(smbclient)
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : syntax-highlighting-dev
BuildRequires : taglib-dev

%description
KFileAudioPreview is a plugin for the KFileMetaPreview class in KIO to
allow audio files to be previewed in places like the file open dialog.

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
%setup -q -n kio-extras-21.12.1
cd %{_builddir}/kio-extras-21.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641955657
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake .. -DLIBSSH_LIBRARIES="-lssh"
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1641955657
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kio-extras
cp %{_builddir}/kio-extras-21.12.1/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kio-extras/52039e5c19c950d4c7d6ec5da42ebba2c6def7ee
cp %{_builddir}/kio-extras-21.12.1/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kio-extras/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/kio-extras-21.12.1/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kio-extras/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/kio-extras-21.12.1/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kio-extras/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/kio-extras-21.12.1/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kio-extras/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/kio-extras-21.12.1/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kio-extras/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/kio-extras-21.12.1/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/kio-extras/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/kio-extras-21.12.1/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kio-extras/a4c60b3fefda228cd7439d3565df043192fef137
cp %{_builddir}/kio-extras-21.12.1/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kio-extras/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kio-extras-21.12.1/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kio-extras/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
cp %{_builddir}/kio-extras-21.12.1/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kio-extras/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
cp %{_builddir}/kio-extras-21.12.1/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kio-extras/19d98e1b6f8ef12849ea4012a052d3907f336c91
cp %{_builddir}/kio-extras-21.12.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kio-extras/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kio-extras-21.12.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kio-extras/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kio-extras-21.12.1/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kio-extras/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kio-extras-21.12.1/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kio-extras/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kio-extras-21.12.1/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kio-extras/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
cp %{_builddir}/kio-extras-21.12.1/man/LICENSE %{buildroot}/usr/share/package-licenses/kio-extras/67218f86a21c5afe177def300337c7ff8ccf40f9
cp %{_builddir}/kio-extras-21.12.1/smb/kdsoap-ws-discovery-client/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kio-extras/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/kio-extras-21.12.1/smb/kdsoap-ws-discovery-client/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/kio-extras/d2f4aa13872c7286a16003262a345e5c9a49a066
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

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kf5/smbnotifier

%files data
%defattr(-,root,root,-)
/usr/share/config.kcfg/jpegcreatorsettings5.kcfg
/usr/share/dbus-1/services/org.kde.kmtpd5.service
/usr/share/kio_bookmarks/kio_bookmarks.css
/usr/share/kio_docfilter/kio_docfilter.css
/usr/share/kio_info/kde-info2html
/usr/share/kio_info/kde-info2html.conf
/usr/share/konqueror/dirtree/remote/mtp-network.desktop
/usr/share/konqueror/dirtree/remote/smb-network.desktop
/usr/share/kservices5/audiothumbnail.desktop
/usr/share/kservices5/comicbookthumbnail.desktop
/usr/share/kservices5/cursorthumbnail.desktop
/usr/share/kservices5/directorythumbnail.desktop
/usr/share/kservices5/djvuthumbnail.desktop
/usr/share/kservices5/ebookthumbnail.desktop
/usr/share/kservices5/exrthumbnail.desktop
/usr/share/kservices5/imagethumbnail.desktop
/usr/share/kservices5/jpegthumbnail.desktop
/usr/share/kservices5/kraorathumbnail.desktop
/usr/share/kservices5/opendocumentthumbnail.desktop
/usr/share/kservices5/svgthumbnail.desktop
/usr/share/kservices5/textthumbnail.desktop
/usr/share/kservices5/windowsexethumbnail.desktop
/usr/share/kservices5/windowsimagethumbnail.desktop
/usr/share/kservicetypes5/thumbcreator.desktop
/usr/share/qlogging-categories5/kio-extras.categories
/usr/share/qlogging-categories5/kio-extras.renamecategories
/usr/share/remoteview/mtp-network.desktop
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
/usr/share/doc/HTML/ca/kioslave5/zstd/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/zstd/index.docbook
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
/usr/share/doc/HTML/de/kioslave5/zstd/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/zstd/index.docbook
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
/usr/share/doc/HTML/en/kioslave5/zstd/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/zstd/index.docbook
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
/usr/share/doc/HTML/es/kioslave5/nfs/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/nfs/index.docbook
/usr/share/doc/HTML/es/kioslave5/recentdocuments/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/recentdocuments/index.docbook
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
/usr/share/doc/HTML/es/kioslave5/zstd/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/zstd/index.docbook
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
/usr/share/doc/HTML/fr/kioslave5/bookmarks/index.cache.bz2
/usr/share/doc/HTML/fr/kioslave5/bookmarks/index.docbook
/usr/share/doc/HTML/fr/kioslave5/bzip2/index.cache.bz2
/usr/share/doc/HTML/fr/kioslave5/bzip2/index.docbook
/usr/share/doc/HTML/fr/kioslave5/fish/index.cache.bz2
/usr/share/doc/HTML/fr/kioslave5/fish/index.docbook
/usr/share/doc/HTML/fr/kioslave5/gzip/index.cache.bz2
/usr/share/doc/HTML/fr/kioslave5/gzip/index.docbook
/usr/share/doc/HTML/fr/kioslave5/info/index.cache.bz2
/usr/share/doc/HTML/fr/kioslave5/info/index.docbook
/usr/share/doc/HTML/fr/kioslave5/man/index.cache.bz2
/usr/share/doc/HTML/fr/kioslave5/man/index.docbook
/usr/share/doc/HTML/fr/kioslave5/nfs/index.cache.bz2
/usr/share/doc/HTML/fr/kioslave5/nfs/index.docbook
/usr/share/doc/HTML/fr/kioslave5/sftp/index.cache.bz2
/usr/share/doc/HTML/fr/kioslave5/sftp/index.docbook
/usr/share/doc/HTML/fr/kioslave5/tar/index.cache.bz2
/usr/share/doc/HTML/fr/kioslave5/tar/index.docbook
/usr/share/doc/HTML/fr/kioslave5/thumbnail/index.cache.bz2
/usr/share/doc/HTML/fr/kioslave5/thumbnail/index.docbook
/usr/share/doc/HTML/fr/kioslave5/xz/index.cache.bz2
/usr/share/doc/HTML/fr/kioslave5/xz/index.docbook
/usr/share/doc/HTML/gl/kioslave5/bookmarks/index.cache.bz2
/usr/share/doc/HTML/gl/kioslave5/bookmarks/index.docbook
/usr/share/doc/HTML/gl/kioslave5/bzip2/index.cache.bz2
/usr/share/doc/HTML/gl/kioslave5/bzip2/index.docbook
/usr/share/doc/HTML/gl/kioslave5/fish/index.cache.bz2
/usr/share/doc/HTML/gl/kioslave5/fish/index.docbook
/usr/share/doc/HTML/gl/kioslave5/gzip/index.cache.bz2
/usr/share/doc/HTML/gl/kioslave5/gzip/index.docbook
/usr/share/doc/HTML/gl/kioslave5/info/index.cache.bz2
/usr/share/doc/HTML/gl/kioslave5/info/index.docbook
/usr/share/doc/HTML/gl/kioslave5/man/index.cache.bz2
/usr/share/doc/HTML/gl/kioslave5/man/index.docbook
/usr/share/doc/HTML/gl/kioslave5/nfs/index.cache.bz2
/usr/share/doc/HTML/gl/kioslave5/nfs/index.docbook
/usr/share/doc/HTML/gl/kioslave5/sftp/index.cache.bz2
/usr/share/doc/HTML/gl/kioslave5/sftp/index.docbook
/usr/share/doc/HTML/gl/kioslave5/tar/index.cache.bz2
/usr/share/doc/HTML/gl/kioslave5/tar/index.docbook
/usr/share/doc/HTML/gl/kioslave5/xz/index.cache.bz2
/usr/share/doc/HTML/gl/kioslave5/xz/index.docbook
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
/usr/share/doc/HTML/it/kioslave5/zstd/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/zstd/index.docbook
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
/usr/share/doc/HTML/nl/kioslave5/zstd/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/zstd/index.docbook
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
/usr/share/doc/HTML/uk/kioslave5/zstd/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/zstd/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkioarchive.so.5
/usr/lib64/libkioarchive.so.5.97.0
/usr/lib64/qt5/plugins/audiothumbnail.so
/usr/lib64/qt5/plugins/comicbookthumbnail.so
/usr/lib64/qt5/plugins/cursorthumbnail.so
/usr/lib64/qt5/plugins/djvuthumbnail.so
/usr/lib64/qt5/plugins/ebookthumbnail.so
/usr/lib64/qt5/plugins/exrthumbnail.so
/usr/lib64/qt5/plugins/imagethumbnail.so
/usr/lib64/qt5/plugins/jpegthumbnail.so
/usr/lib64/qt5/plugins/kf5/kded/filenamesearchmodule.so
/usr/lib64/qt5/plugins/kf5/kded/recentdocumentsnotifier.so
/usr/lib64/qt5/plugins/kf5/kded/smbwatcher.so
/usr/lib64/qt5/plugins/kf5/kfileitemaction/kactivitymanagerd_fileitem_linking_plugin.so
/usr/lib64/qt5/plugins/kf5/kio/about.so
/usr/lib64/qt5/plugins/kf5/kio/activities.so
/usr/lib64/qt5/plugins/kf5/kio/archive.so
/usr/lib64/qt5/plugins/kf5/kio/bookmarks.so
/usr/lib64/qt5/plugins/kf5/kio/filter.so
/usr/lib64/qt5/plugins/kf5/kio/fish.so
/usr/lib64/qt5/plugins/kf5/kio/info.so
/usr/lib64/qt5/plugins/kf5/kio/kio_filenamesearch.so
/usr/lib64/qt5/plugins/kf5/kio/man.so
/usr/lib64/qt5/plugins/kf5/kio/mtp.so
/usr/lib64/qt5/plugins/kf5/kio/nfs.so
/usr/lib64/qt5/plugins/kf5/kio/recentdocuments.so
/usr/lib64/qt5/plugins/kf5/kio/recentlyused.so
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
/usr/share/package-licenses/kio-extras/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/kio-extras/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kio-extras/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kio-extras/52039e5c19c950d4c7d6ec5da42ebba2c6def7ee
/usr/share/package-licenses/kio-extras/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kio-extras/67218f86a21c5afe177def300337c7ff8ccf40f9
/usr/share/package-licenses/kio-extras/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kio-extras/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/kio-extras/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kio-extras/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kio-extras/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/kio-extras/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/kio-extras/d2f4aa13872c7286a16003262a345e5c9a49a066
/usr/share/package-licenses/kio-extras/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kio-extras/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kfileaudiopreview5.lang -f kio5_activities.lang -f kio5_archive.lang -f kio5_bookmarks.lang -f kio5_fish.lang -f kio5_info.lang -f kio5_man.lang -f kio5_mtp.lang -f kio5_nfs.lang -f kio5_recentdocuments.lang -f kio5_sftp.lang -f kio5_smb.lang -f kio5_thumbnail.lang
%defattr(-,root,root,-)

