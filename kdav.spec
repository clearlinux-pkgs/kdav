#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kdav
Version  : 19.12.2
Release  : 18
URL      : https://download.kde.org/stable/release-service/19.12.2/src/kdav-19.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.2/src/kdav-19.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.2/src/kdav-19.12.2.tar.xz.sig
Summary  : A DAV protocol implemention with KJobs
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: kdav-data = %{version}-%{release}
Requires: kdav-lib = %{version}-%{release}
Requires: kdav-license = %{version}-%{release}
Requires: kdav-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
# KDAV
## What's this?
This is an DAV protocol implemention with KJobs.
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
%setup -q -n kdav-19.12.2
cd %{_builddir}/kdav-19.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581017594
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
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1581017594
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdav
cp %{_builddir}/kdav-19.12.2/COPYING %{buildroot}/usr/share/package-licenses/kdav/7e52b139aa82028afadf25f4b534d2404bf97cca
cp %{_builddir}/kdav-19.12.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/kdav/ba8966e2473a9969bdcab3dc82274c817cfd98a1
pushd clr-build
%make_install
popd
%find_lang libkdav

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kdav.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim/KDAV/DavCollection
/usr/include/KPim/KDAV/DavCollectionDeleteJob
/usr/include/KPim/KDAV/DavCollectionModifyJob
/usr/include/KPim/KDAV/DavCollectionsFetchJob
/usr/include/KPim/KDAV/DavCollectionsMultiFetchJob
/usr/include/KPim/KDAV/DavError
/usr/include/KPim/KDAV/DavItem
/usr/include/KPim/KDAV/DavItemCreateJob
/usr/include/KPim/KDAV/DavItemDeleteJob
/usr/include/KPim/KDAV/DavItemFetchJob
/usr/include/KPim/KDAV/DavItemModifyJob
/usr/include/KPim/KDAV/DavItemsFetchJob
/usr/include/KPim/KDAV/DavItemsListJob
/usr/include/KPim/KDAV/DavJobBase
/usr/include/KPim/KDAV/DavPrincipalHomesetsFetchJob
/usr/include/KPim/KDAV/DavPrincipalSearchJob
/usr/include/KPim/KDAV/DavUrl
/usr/include/KPim/KDAV/Enums
/usr/include/KPim/KDAV/EtagCache
/usr/include/KPim/KDAV/ProtocolInfo
/usr/include/KPim/kdav/davcollection.h
/usr/include/KPim/kdav/davcollectiondeletejob.h
/usr/include/KPim/kdav/davcollectionmodifyjob.h
/usr/include/KPim/kdav/davcollectionsfetchjob.h
/usr/include/KPim/kdav/davcollectionsmultifetchjob.h
/usr/include/KPim/kdav/daverror.h
/usr/include/KPim/kdav/davitem.h
/usr/include/KPim/kdav/davitemcreatejob.h
/usr/include/KPim/kdav/davitemdeletejob.h
/usr/include/KPim/kdav/davitemfetchjob.h
/usr/include/KPim/kdav/davitemmodifyjob.h
/usr/include/KPim/kdav/davitemsfetchjob.h
/usr/include/KPim/kdav/davitemslistjob.h
/usr/include/KPim/kdav/davjobbase.h
/usr/include/KPim/kdav/davprincipalhomesetsfetchjob.h
/usr/include/KPim/kdav/davprincipalsearchjob.h
/usr/include/KPim/kdav/davurl.h
/usr/include/KPim/kdav/enums.h
/usr/include/KPim/kdav/etagcache.h
/usr/include/KPim/kdav/kpimkdav_export.h
/usr/include/KPim/kdav/protocolinfo.h
/usr/include/KPim/kpimkdav_version.h
/usr/lib64/cmake/KPimKDAV/KPimKDAVConfig.cmake
/usr/lib64/cmake/KPimKDAV/KPimKDAVConfigVersion.cmake
/usr/lib64/cmake/KPimKDAV/KPimKDAVTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPimKDAV/KPimKDAVTargets.cmake
/usr/lib64/libKPimKDAV.so
/usr/lib64/qt5/mkspecs/modules/qt_kdav.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKPimKDAV.so.5
/usr/lib64/libKPimKDAV.so.5.13.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdav/7e52b139aa82028afadf25f4b534d2404bf97cca
/usr/share/package-licenses/kdav/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f libkdav.lang
%defattr(-,root,root,-)

