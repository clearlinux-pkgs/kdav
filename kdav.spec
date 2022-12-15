#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kdav
Version  : 5.101.0
Release  : 47
URL      : https://download.kde.org/stable/frameworks/5.101/kdav-5.101.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.101/kdav-5.101.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.101/kdav-5.101.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.0
Requires: kdav-data = %{version}-%{release}
Requires: kdav-lib = %{version}-%{release}
Requires: kdav-license = %{version}-%{release}
Requires: kdav-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kio-dev

%description
# KDAV
## Introduction
This is an DAV protocol implementation with KJobs.
Calendars and todos are supported, using either GroupDAV
or CalDAV, and contacts are supported using GroupDAV or
CardDAV.

%package data
Summary: data components for the kdav package.
Group: Data

%description data
data components for the kdav package.


%package dev
Summary: dev components for the kdav package.
Group: Development
Requires: kdav-lib = %{version}-%{release}
Requires: kdav-data = %{version}-%{release}
Provides: kdav-devel = %{version}-%{release}
Requires: kdav = %{version}-%{release}

%description dev
dev components for the kdav package.


%package lib
Summary: lib components for the kdav package.
Group: Libraries
Requires: kdav-data = %{version}-%{release}
Requires: kdav-license = %{version}-%{release}

%description lib
lib components for the kdav package.


%package license
Summary: license components for the kdav package.
Group: Default

%description license
license components for the kdav package.


%package locales
Summary: locales components for the kdav package.
Group: Default

%description locales
locales components for the kdav package.


%prep
%setup -q -n kdav-5.101.0
cd %{_builddir}/kdav-5.101.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671124594
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
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1671124594
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdav
cp %{_builddir}/kdav-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdav/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kdav-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdav/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kdav-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdav/20079e8f79713dce80ab09774505773c926afa2a || :
pushd clr-build
%make_install
popd
%find_lang libkdav

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kdav.categories
/usr/share/qlogging-categories5/kdav.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KDAV/KDAV/DavCollection
/usr/include/KF5/KDAV/KDAV/DavCollectionDeleteJob
/usr/include/KF5/KDAV/KDAV/DavCollectionModifyJob
/usr/include/KF5/KDAV/KDAV/DavCollectionsFetchJob
/usr/include/KF5/KDAV/KDAV/DavCollectionsMultiFetchJob
/usr/include/KF5/KDAV/KDAV/DavError
/usr/include/KF5/KDAV/KDAV/DavItem
/usr/include/KF5/KDAV/KDAV/DavItemCreateJob
/usr/include/KF5/KDAV/KDAV/DavItemDeleteJob
/usr/include/KF5/KDAV/KDAV/DavItemFetchJob
/usr/include/KF5/KDAV/KDAV/DavItemModifyJob
/usr/include/KF5/KDAV/KDAV/DavItemsFetchJob
/usr/include/KF5/KDAV/KDAV/DavItemsListJob
/usr/include/KF5/KDAV/KDAV/DavJobBase
/usr/include/KF5/KDAV/KDAV/DavPrincipalHomesetsFetchJob
/usr/include/KF5/KDAV/KDAV/DavPrincipalSearchJob
/usr/include/KF5/KDAV/KDAV/DavUrl
/usr/include/KF5/KDAV/KDAV/Enums
/usr/include/KF5/KDAV/KDAV/EtagCache
/usr/include/KF5/KDAV/KDAV/ProtocolInfo
/usr/include/KF5/KDAV/kdav/davcollection.h
/usr/include/KF5/KDAV/kdav/davcollectiondeletejob.h
/usr/include/KF5/KDAV/kdav/davcollectionmodifyjob.h
/usr/include/KF5/KDAV/kdav/davcollectionsfetchjob.h
/usr/include/KF5/KDAV/kdav/davcollectionsmultifetchjob.h
/usr/include/KF5/KDAV/kdav/daverror.h
/usr/include/KF5/KDAV/kdav/davitem.h
/usr/include/KF5/KDAV/kdav/davitemcreatejob.h
/usr/include/KF5/KDAV/kdav/davitemdeletejob.h
/usr/include/KF5/KDAV/kdav/davitemfetchjob.h
/usr/include/KF5/KDAV/kdav/davitemmodifyjob.h
/usr/include/KF5/KDAV/kdav/davitemsfetchjob.h
/usr/include/KF5/KDAV/kdav/davitemslistjob.h
/usr/include/KF5/KDAV/kdav/davjobbase.h
/usr/include/KF5/KDAV/kdav/davprincipalhomesetsfetchjob.h
/usr/include/KF5/KDAV/kdav/davprincipalsearchjob.h
/usr/include/KF5/KDAV/kdav/davurl.h
/usr/include/KF5/KDAV/kdav/enums.h
/usr/include/KF5/KDAV/kdav/etagcache.h
/usr/include/KF5/KDAV/kdav/kdav_export.h
/usr/include/KF5/KDAV/kdav/protocolinfo.h
/usr/include/KF5/KDAV/kdav_version.h
/usr/lib64/cmake/KF5DAV/KF5DAVConfig.cmake
/usr/lib64/cmake/KF5DAV/KF5DAVConfigVersion.cmake
/usr/lib64/cmake/KF5DAV/KF5DAVTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5DAV/KF5DAVTargets.cmake
/usr/lib64/libKF5DAV.so
/usr/lib64/qt5/mkspecs/modules/qt_KDAV.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5DAV.so.5
/usr/lib64/libKF5DAV.so.5.101.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdav/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kdav/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kdav/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libkdav.lang
%defattr(-,root,root,-)

