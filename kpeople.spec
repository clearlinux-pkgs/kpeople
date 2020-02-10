#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kpeople
Version  : 5.67.0
Release  : 24
URL      : https://download.kde.org/stable/frameworks/5.67/kpeople-5.67.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.67/kpeople-5.67.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.67/kpeople-5.67.0.tar.xz.sig
Summary  : A library that provides access to all contacts and the people who hold them
Group    : Development/Tools
License  : LGPL-2.1
Requires: kpeople-data = %{version}-%{release}
Requires: kpeople-lib = %{version}-%{release}
Requires: kpeople-license = %{version}-%{release}
Requires: kpeople-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
# KPeople
Provides access to all contacts and aggregates them by person.
## Introduction

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
%setup -q -n kpeople-5.67.0
cd %{_builddir}/kpeople-5.67.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581372106
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
export SOURCE_DATE_EPOCH=1581372106
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kpeople
cp %{_builddir}/kpeople-5.67.0/COPYING %{buildroot}/usr/share/package-licenses/kpeople/01a6b4bf79aca9b556822601186afab86e8c4fbf
pushd clr-build
%make_install
popd
%find_lang kpeople5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservicetypes5/kpeople_data_source.desktop
/usr/share/kservicetypes5/kpeople_plugin.desktop
/usr/share/kservicetypes5/persondetailsplugin.desktop
/usr/share/qlogging-categories5/kpeople.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KPeople/KPeople/Global
/usr/include/KF5/KPeople/KPeople/PersonData
/usr/include/KF5/KPeople/KPeople/PersonPluginManager
/usr/include/KF5/KPeople/KPeople/PersonsModel
/usr/include/KF5/KPeople/KPeople/Widgets/AbstractFieldWidgetFactory
/usr/include/KF5/KPeople/KPeople/Widgets/Actions
/usr/include/KF5/KPeople/KPeople/Widgets/MergeDialog
/usr/include/KF5/KPeople/KPeople/Widgets/PersonDetailsDialog
/usr/include/KF5/KPeople/KPeople/Widgets/PersonDetailsView
/usr/include/KF5/KPeople/KPeopleBackend/AbstractContact
/usr/include/KF5/KPeople/KPeopleBackend/AbstractEditableContact
/usr/include/KF5/KPeople/KPeopleBackend/AbstractPersonAction
/usr/include/KF5/KPeople/KPeopleBackend/AllContactsMonitor
/usr/include/KF5/KPeople/KPeopleBackend/BasePersonsDataSource
/usr/include/KF5/KPeople/KPeopleBackend/ContactMonitor
/usr/include/KF5/KPeople/kpeople/global.h
/usr/include/KF5/KPeople/kpeople/kpeople_export.h
/usr/include/KF5/KPeople/kpeople/persondata.h
/usr/include/KF5/KPeople/kpeople/personpluginmanager.h
/usr/include/KF5/KPeople/kpeople/personsmodel.h
/usr/include/KF5/KPeople/kpeople/widgets/abstractfieldwidgetfactory.h
/usr/include/KF5/KPeople/kpeople/widgets/actions.h
/usr/include/KF5/KPeople/kpeople/widgets/kpeoplewidgets_export.h
/usr/include/KF5/KPeople/kpeople/widgets/mergedialog.h
/usr/include/KF5/KPeople/kpeople/widgets/persondetailsdialog.h
/usr/include/KF5/KPeople/kpeople/widgets/persondetailsview.h
/usr/include/KF5/KPeople/kpeoplebackend/abstractcontact.h
/usr/include/KF5/KPeople/kpeoplebackend/abstracteditablecontact.h
/usr/include/KF5/KPeople/kpeoplebackend/abstractpersonaction.h
/usr/include/KF5/KPeople/kpeoplebackend/allcontactsmonitor.h
/usr/include/KF5/KPeople/kpeoplebackend/basepersonsdatasource.h
/usr/include/KF5/KPeople/kpeoplebackend/contactmonitor.h
/usr/include/KF5/KPeople/kpeoplebackend/kpeoplebackend_export.h
/usr/lib64/cmake/KF5People/KF5PeopleConfig.cmake
/usr/lib64/cmake/KF5People/KF5PeopleConfigVersion.cmake
/usr/lib64/cmake/KF5People/KPeopleTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5People/KPeopleTargets.cmake
/usr/lib64/libKF5People.so
/usr/lib64/libKF5PeopleBackend.so
/usr/lib64/libKF5PeopleWidgets.so
/usr/lib64/qt5/mkspecs/modules/qt_KPeople.pri
/usr/lib64/qt5/mkspecs/modules/qt_KPeopleWidgets.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5People.so.5
/usr/lib64/libKF5People.so.5.67.0
/usr/lib64/libKF5PeopleBackend.so.5
/usr/lib64/libKF5PeopleBackend.so.5.67.0
/usr/lib64/libKF5PeopleWidgets.so.5
/usr/lib64/libKF5PeopleWidgets.so.5.67.0
/usr/lib64/qt5/qml/org/kde/people/libKF5PeopleDeclarative.so
/usr/lib64/qt5/qml/org/kde/people/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kpeople/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files locales -f kpeople5.lang
%defattr(-,root,root,-)

