#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kio-extras
Version  : 18.04.3
Release  : 1
URL      : https://github.com/KDE/kio-extras/archive/v18.04.3.tar.gz
Source0  : https://github.com/KDE/kio-extras/archive/v18.04.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 MIT
Requires: kio-extras-lib
Requires: kio-extras-data
Requires: kio-extras-license
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : gperf
BuildRequires : karchive-dev
BuildRequires : kbookmarks-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kdnssd-dev
BuildRequires : kguiaddons-dev
BuildRequires : kiconthemes-dev
BuildRequires : kio-dev
BuildRequires : kitemviews-dev
BuildRequires : kjobwidgets-dev
BuildRequires : kpty-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : phonon-dev
BuildRequires : pkgconfig(libmtp)
BuildRequires : pkgconfig(smbclient)
BuildRequires : shared-mime-info
BuildRequires : solid-dev

%description
This contains a kio slave for NFS version 2 and 3.
Mathias

%package data
Summary: data components for the kio-extras package.
Group: Data

%description data
data components for the kio-extras package.


%package dev
Summary: dev components for the kio-extras package.
Group: Development
Requires: kio-extras-lib
Requires: kio-extras-data
Provides: kio-extras-devel

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
Requires: kio-extras-data
Requires: kio-extras-license

%description lib
lib components for the kio-extras package.


%package license
Summary: license components for the kio-extras package.
Group: Default

%description license
license components for the kio-extras package.


%prep
%setup -q -n kio-extras-18.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532200121
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1532200121
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kio-extras
cp mtp/LICENCE %{buildroot}/usr/share/doc/kio-extras/mtp_LICENCE
cp mtp/COPYING %{buildroot}/usr/share/doc/kio-extras/mtp_COPYING
cp man/LICENSE %{buildroot}/usr/share/doc/kio-extras/man_LICENSE
cp fish/COPYING %{buildroot}/usr/share/doc/kio-extras/fish_COPYING
cp cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/doc/kio-extras/cmake_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/config.kcfg/jpegcreatorsettings5.kcfg
/usr/share/dbus-1/interfaces/kf5_org.kde.network.kioslavenotifier.xml
/usr/share/kio_bookmarks/kio_bookmarks.css
/usr/share/kio_docfilter/kio_docfilter.css
/usr/share/kio_info/kde-info2html
/usr/share/kio_info/kde-info2html.conf
/usr/share/konqsidebartng/virtual_folders/remote/virtualfolder_network.desktop
/usr/share/konqueror/dirtree/remote/mtp-network.desktop
/usr/share/konqueror/dirtree/remote/smb-network.desktop
/usr/share/kservices5/about.protocol
/usr/share/kservices5/ar.protocol
/usr/share/kservices5/bookmarks.protocol
/usr/share/kservices5/bzip.protocol
/usr/share/kservices5/bzip2.protocol
/usr/share/kservices5/comicbookthumbnail.desktop
/usr/share/kservices5/directorythumbnail.desktop
/usr/share/kservices5/djvuthumbnail.desktop
/usr/share/kservices5/filenamesearch.protocol
/usr/share/kservices5/fish.protocol
/usr/share/kservices5/gzip.protocol
/usr/share/kservices5/imagethumbnail.desktop
/usr/share/kservices5/info.protocol
/usr/share/kservices5/jpegthumbnail.desktop
/usr/share/kservices5/kraorathumbnail.desktop
/usr/share/kservices5/lzma.protocol
/usr/share/kservices5/mtp.protocol
/usr/share/kservices5/network.protocol
/usr/share/kservices5/nfs.protocol
/usr/share/kservices5/recentdocuments.protocol
/usr/share/kservices5/settings.protocol
/usr/share/kservices5/smb.protocol
/usr/share/kservices5/svgthumbnail.desktop
/usr/share/kservices5/tar.protocol
/usr/share/kservices5/textthumbnail.desktop
/usr/share/kservices5/thumbnail.protocol
/usr/share/kservices5/windowsexethumbnail.desktop
/usr/share/kservices5/windowsimagethumbnail.desktop
/usr/share/kservices5/xz.protocol
/usr/share/kservices5/zip.protocol
/usr/share/kservicetypes5/thumbcreator.desktop
/usr/share/mime/packages/kf5_network.xml
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
%doc /usr/share/doc/kio\-extras/*
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkioarchive.so.5
/usr/lib64/libkioarchive.so.5.97.0
/usr/lib64/libmolletnetwork5.so.18
/usr/lib64/libmolletnetwork5.so.18.04.3
/usr/lib64/qt5/plugins/comicbookthumbnail.so
/usr/lib64/qt5/plugins/djvuthumbnail.so
/usr/lib64/qt5/plugins/imagethumbnail.so
/usr/lib64/qt5/plugins/jpegthumbnail.so
/usr/lib64/qt5/plugins/kf5/kded/filenamesearchmodule.so
/usr/lib64/qt5/plugins/kf5/kded/networkwatcher.so
/usr/lib64/qt5/plugins/kf5/kded/recentdocumentsnotifier.so
/usr/lib64/qt5/plugins/kf5/kio/archive.so
/usr/lib64/qt5/plugins/kf5/kio/bookmarks.so
/usr/lib64/qt5/plugins/kf5/kio/filenamesearch.so
/usr/lib64/qt5/plugins/kf5/kio/filter.so
/usr/lib64/qt5/plugins/kf5/kio/fish.so
/usr/lib64/qt5/plugins/kf5/kio/info.so
/usr/lib64/qt5/plugins/kf5/kio/mtp.so
/usr/lib64/qt5/plugins/kf5/kio/network.so
/usr/lib64/qt5/plugins/kf5/kio/nfs.so
/usr/lib64/qt5/plugins/kf5/kio/recentdocuments.so
/usr/lib64/qt5/plugins/kf5/kio/settings.so
/usr/lib64/qt5/plugins/kf5/kio/smb.so
/usr/lib64/qt5/plugins/kf5/kio/thumbnail.so
/usr/lib64/qt5/plugins/kfileaudiopreview.so
/usr/lib64/qt5/plugins/kritathumbnail.so
/usr/lib64/qt5/plugins/libkio_about.so
/usr/lib64/qt5/plugins/svgthumbnail.so
/usr/lib64/qt5/plugins/textthumbnail.so
/usr/lib64/qt5/plugins/windowsexethumbnail.so
/usr/lib64/qt5/plugins/windowsimagethumbnail.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/kio-extras/cmake_COPYING-CMAKE-SCRIPTS
/usr/share/doc/kio-extras/fish_COPYING
/usr/share/doc/kio-extras/man_LICENSE
/usr/share/doc/kio-extras/mtp_COPYING
