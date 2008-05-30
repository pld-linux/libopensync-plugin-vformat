Summary:	OpenSync vFormat Plugin
Summary(pl.UTF-8):	Wtyczka vFormat dla szkieletu OpenSync
Name:		libopensync-plugin-vformat
Version:	0.36
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.opensync.org/download/releases/0.36/%{name}-%{version}.tar.bz2
# Source0-md5:	f3d1efdc1e7142fc74364e92f2066ee0
URL:		http://www.opensync.org/
BuildRequires:	glib2-devel >= 1:2.4
BuildRequires:	libopensync-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	cmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and
distribution independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains vFormat plugin for OpenSync framework.

%description -l pl.UTF-8
OpenSync to niezależny od platformy i dystrybucji szkielet do
synchronizacji danych.

Składa się z różnych wtyczek, których można używać do łączenia z
urządzeniami, potężnego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera wtyczkę vFormat dla szkieletu OpenSync.

%prep
%setup -q

%build
mkdir build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/vconvert
%attr(755,root,root) %{_libdir}/opensync-1.0/formats/*.so
