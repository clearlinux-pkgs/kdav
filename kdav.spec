#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kdav
Version  : 6.5.0
Release  : 76
URL      : https://download.kde.org/stable/frameworks/6.5/kdav-6.5.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.5/kdav-6.5.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.5/kdav-6.5.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
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
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kdav-6.5.0
cd %{_builddir}/kdav-6.5.0
pushd ..
cp -a kdav-6.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1723478863
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1723478863
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdav
cp %{_builddir}/kdav-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdav/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kdav-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdav/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kdav-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdav/20079e8f79713dce80ab09774505773c926afa2a || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libkdav6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kdav.categories
/usr/share/qlogging-categories6/kdav.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KDAV/KDAV/DavCollection
/usr/include/KF6/KDAV/KDAV/DavCollectionDeleteJob
/usr/include/KF6/KDAV/KDAV/DavCollectionModifyJob
/usr/include/KF6/KDAV/KDAV/DavCollectionsFetchJob
/usr/include/KF6/KDAV/KDAV/DavCollectionsMultiFetchJob
/usr/include/KF6/KDAV/KDAV/DavError
/usr/include/KF6/KDAV/KDAV/DavItem
/usr/include/KF6/KDAV/KDAV/DavItemCreateJob
/usr/include/KF6/KDAV/KDAV/DavItemDeleteJob
/usr/include/KF6/KDAV/KDAV/DavItemFetchJob
/usr/include/KF6/KDAV/KDAV/DavItemModifyJob
/usr/include/KF6/KDAV/KDAV/DavItemsFetchJob
/usr/include/KF6/KDAV/KDAV/DavItemsListJob
/usr/include/KF6/KDAV/KDAV/DavJobBase
/usr/include/KF6/KDAV/KDAV/DavPrincipalHomesetsFetchJob
/usr/include/KF6/KDAV/KDAV/DavPrincipalSearchJob
/usr/include/KF6/KDAV/KDAV/DavUrl
/usr/include/KF6/KDAV/KDAV/Enums
/usr/include/KF6/KDAV/KDAV/EtagCache
/usr/include/KF6/KDAV/KDAV/ProtocolInfo
/usr/include/KF6/KDAV/kdav/davcollection.h
/usr/include/KF6/KDAV/kdav/davcollectiondeletejob.h
/usr/include/KF6/KDAV/kdav/davcollectionmodifyjob.h
/usr/include/KF6/KDAV/kdav/davcollectionsfetchjob.h
/usr/include/KF6/KDAV/kdav/davcollectionsmultifetchjob.h
/usr/include/KF6/KDAV/kdav/daverror.h
/usr/include/KF6/KDAV/kdav/davitem.h
/usr/include/KF6/KDAV/kdav/davitemcreatejob.h
/usr/include/KF6/KDAV/kdav/davitemdeletejob.h
/usr/include/KF6/KDAV/kdav/davitemfetchjob.h
/usr/include/KF6/KDAV/kdav/davitemmodifyjob.h
/usr/include/KF6/KDAV/kdav/davitemsfetchjob.h
/usr/include/KF6/KDAV/kdav/davitemslistjob.h
/usr/include/KF6/KDAV/kdav/davjobbase.h
/usr/include/KF6/KDAV/kdav/davprincipalhomesetsfetchjob.h
/usr/include/KF6/KDAV/kdav/davprincipalsearchjob.h
/usr/include/KF6/KDAV/kdav/davurl.h
/usr/include/KF6/KDAV/kdav/enums.h
/usr/include/KF6/KDAV/kdav/etagcache.h
/usr/include/KF6/KDAV/kdav/kdav_export.h
/usr/include/KF6/KDAV/kdav/protocolinfo.h
/usr/include/KF6/KDAV/kdav_version.h
/usr/lib64/cmake/KF6DAV/KF6DAVConfig.cmake
/usr/lib64/cmake/KF6DAV/KF6DAVConfigVersion.cmake
/usr/lib64/cmake/KF6DAV/KF6DAVTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6DAV/KF6DAVTargets.cmake
/usr/lib64/libKF6DAV.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6DAV.so.6.5.0
/usr/lib64/libKF6DAV.so.6
/usr/lib64/libKF6DAV.so.6.5.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdav/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kdav/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kdav/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libkdav6.lang
%defattr(-,root,root,-)

