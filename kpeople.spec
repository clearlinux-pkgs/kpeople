#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v5
# autospec commit: c02b2fe
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kpeople
Version  : 6.0.0
Release  : 75
URL      : https://download.kde.org/stable/frameworks/6.0/kpeople-6.0.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.0/kpeople-6.0.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.0/kpeople-6.0.0.tar.xz.sig
Summary  : A library that provides access to all contacts and the people who hold them
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.1
Requires: kpeople-data = %{version}-%{release}
Requires: kpeople-lib = %{version}-%{release}
Requires: kpeople-license = %{version}-%{release}
Requires: kpeople-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcontacts-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description


%package data
Summary: data components for the kpeople package.
Group: Data

%description data
data components for the kpeople package.


%package dev
Summary: dev components for the kpeople package.
Group: Development
Requires: kpeople-lib = %{version}-%{release}
Requires: kpeople-data = %{version}-%{release}
Provides: kpeople-devel = %{version}-%{release}
Requires: kpeople = %{version}-%{release}

%description dev
dev components for the kpeople package.


%package lib
Summary: lib components for the kpeople package.
Group: Libraries
Requires: kpeople-data = %{version}-%{release}
Requires: kpeople-license = %{version}-%{release}

%description lib
lib components for the kpeople package.


%package license
Summary: license components for the kpeople package.
Group: Default

%description license
license components for the kpeople package.


%package locales
Summary: locales components for the kpeople package.
Group: Default

%description locales
locales components for the kpeople package.


%prep
%setup -q -n kpeople-6.0.0
cd %{_builddir}/kpeople-6.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711147099
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
%cmake ..
make  %{?_smp_mflags}
popd
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
%cmake ..
make  %{?_smp_mflags}
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
export SOURCE_DATE_EPOCH=1711147099
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kpeople
cp %{_builddir}/kpeople-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kpeople/3630f1ffcec0e075bf446b88c7b507b1287b571d || :
cp %{_builddir}/kpeople-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kpeople/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kpeople-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kpeople/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kpeople-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kpeople/37d1ccdb1e19e25429b2c910ddfef5c7242f7b62 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kpeople6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kpeople.categories
/usr/share/qlogging-categories6/kpeople.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KPeople/KPeople/Actions
/usr/include/KF6/KPeople/KPeople/Global
/usr/include/KF6/KPeople/KPeople/PersonData
/usr/include/KF6/KPeople/KPeople/PersonPluginManager
/usr/include/KF6/KPeople/KPeople/PersonsModel
/usr/include/KF6/KPeople/KPeople/PersonsSortFilterProxyModel
/usr/include/KF6/KPeople/KPeople/Widgets/AbstractFieldWidgetFactory
/usr/include/KF6/KPeople/KPeople/Widgets/MergeDialog
/usr/include/KF6/KPeople/KPeople/Widgets/PersonDetailsDialog
/usr/include/KF6/KPeople/KPeople/Widgets/PersonDetailsView
/usr/include/KF6/KPeople/KPeopleBackend/AbstractContact
/usr/include/KF6/KPeople/KPeopleBackend/AbstractEditableContact
/usr/include/KF6/KPeople/KPeopleBackend/AbstractPersonAction
/usr/include/KF6/KPeople/KPeopleBackend/AllContactsMonitor
/usr/include/KF6/KPeople/KPeopleBackend/BasePersonsDataSource
/usr/include/KF6/KPeople/KPeopleBackend/ContactMonitor
/usr/include/KF6/KPeople/kpeople/actions.h
/usr/include/KF6/KPeople/kpeople/global.h
/usr/include/KF6/KPeople/kpeople/kpeople_export.h
/usr/include/KF6/KPeople/kpeople/persondata.h
/usr/include/KF6/KPeople/kpeople/personpluginmanager.h
/usr/include/KF6/KPeople/kpeople/personsmodel.h
/usr/include/KF6/KPeople/kpeople/personssortfilterproxymodel.h
/usr/include/KF6/KPeople/kpeople/widgets/abstractfieldwidgetfactory.h
/usr/include/KF6/KPeople/kpeople/widgets/kpeoplewidgets_export.h
/usr/include/KF6/KPeople/kpeople/widgets/mergedialog.h
/usr/include/KF6/KPeople/kpeople/widgets/persondetailsdialog.h
/usr/include/KF6/KPeople/kpeople/widgets/persondetailsview.h
/usr/include/KF6/KPeople/kpeople_version.h
/usr/include/KF6/KPeople/kpeoplebackend/abstractcontact.h
/usr/include/KF6/KPeople/kpeoplebackend/abstracteditablecontact.h
/usr/include/KF6/KPeople/kpeoplebackend/abstractpersonaction.h
/usr/include/KF6/KPeople/kpeoplebackend/allcontactsmonitor.h
/usr/include/KF6/KPeople/kpeoplebackend/basepersonsdatasource.h
/usr/include/KF6/KPeople/kpeoplebackend/contactmonitor.h
/usr/include/KF6/KPeople/kpeoplebackend/kpeoplebackend_export.h
/usr/include/KF6/KPeople/kpeopleprivate/personmanager_p.h
/usr/lib64/cmake/KF6People/KF6PeopleConfig.cmake
/usr/lib64/cmake/KF6People/KF6PeopleConfigVersion.cmake
/usr/lib64/cmake/KF6People/KPeopleTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6People/KPeopleTargets.cmake
/usr/lib64/libKF6People.so
/usr/lib64/libKF6PeopleBackend.so
/usr/lib64/libKF6PeopleWidgets.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6People.so.6.0.0
/V3/usr/lib64/libKF6PeopleBackend.so.6.0.0
/V3/usr/lib64/libKF6PeopleWidgets.so.6.0.0
/V3/usr/lib64/qt6/plugins/kpeople/datasource/KPeopleVCard.so
/V3/usr/lib64/qt6/qml/org/kde/people/libKF6PeopleDeclarative.so
/usr/lib64/libKF6People.so.6
/usr/lib64/libKF6People.so.6.0.0
/usr/lib64/libKF6PeopleBackend.so.6
/usr/lib64/libKF6PeopleBackend.so.6.0.0
/usr/lib64/libKF6PeopleWidgets.so.6
/usr/lib64/libKF6PeopleWidgets.so.6.0.0
/usr/lib64/qt6/plugins/kpeople/datasource/KPeopleVCard.so
/usr/lib64/qt6/qml/org/kde/people/libKF6PeopleDeclarative.so
/usr/lib64/qt6/qml/org/kde/people/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kpeople/3630f1ffcec0e075bf446b88c7b507b1287b571d
/usr/share/package-licenses/kpeople/37d1ccdb1e19e25429b2c910ddfef5c7242f7b62
/usr/share/package-licenses/kpeople/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kpeople/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files locales -f kpeople6.lang
%defattr(-,root,root,-)

