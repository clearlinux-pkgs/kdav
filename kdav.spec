#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kdav
Version  : 18.12.2
Release  : 4
URL      : https://download.kde.org/stable/applications/18.12.2/src/kdav-18.12.2.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.2/src/kdav-18.12.2.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.2/src/kdav-18.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: kdav-data = %{version}-%{release}
Requires: kdav-lib = %{version}-%{release}
Requires: kdav-license = %{version}-%{release}
Requires: kdav-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
==== What's this ? ====
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
%setup -q -n kdav-18.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549882701
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549882701
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdav
cp COPYING %{buildroot}/usr/share/package-licenses/kdav/COPYING
pushd clr-build
%make_install
popd
%find_lang libkdav

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/xdg/kdav.categories

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
/usr/include/KPim/KDAV/DavManager
/usr/include/KPim/KDAV/DavPrincipalHomesetsFetchJob
/usr/include/KPim/KDAV/DavPrincipalSearchJob
/usr/include/KPim/KDAV/DavProtocolBase
/usr/include/KPim/KDAV/DavUrl
/usr/include/KPim/KDAV/Enums
/usr/include/KPim/KDAV/EtagCache
/usr/include/KPim/KDAV/Utils
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
/usr/include/KPim/kdav/davmanager.h
/usr/include/KPim/kdav/davprincipalhomesetsfetchjob.h
/usr/include/KPim/kdav/davprincipalsearchjob.h
/usr/include/KPim/kdav/davprotocolbase.h
/usr/include/KPim/kdav/davurl.h
/usr/include/KPim/kdav/enums.h
/usr/include/KPim/kdav/etagcache.h
/usr/include/KPim/kdav/kpimkdav_export.h
/usr/include/KPim/kdav/libkdav_debug.h
/usr/include/KPim/kdav/utils.h
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
/usr/lib64/libKPimKDAV.so.5.10.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdav/COPYING

%files locales -f libkdav.lang
%defattr(-,root,root,-)

