Summary:	OpenSync vFormat Plugin
Summary(pl.UTF-8):	Wtyczka vFormat dla szkieletu OpenSync
Name:		libopensync-plugin-vformat
Version:	0.39
Release:	1
License:	LGPL v2.1+
Group:		Libraries
# originally http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	2c4e179fd6e9e07e1af136c23a9b49c8
# dead domain
#URL:		http://www.opensync.org/
BuildRequires:	cmake >= 2.4.4
BuildRequires:	glib2-devel >= 1:2.4
BuildRequires:	libopensync-devel >= 1:%{version}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	glib2 >= 1:2.4
Requires:	libopensync >= 1:%{version}
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
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/vconvert
%attr(755,root,root) %{_libdir}/libopensync1/formats/vcard.so
%attr(755,root,root) %{_libdir}/libopensync1/formats/vevent.so
%attr(755,root,root) %{_libdir}/libopensync1/formats/vformat-xmlformat.so
%attr(755,root,root) %{_libdir}/libopensync1/formats/vjournal.so
%attr(755,root,root) %{_libdir}/libopensync1/formats/vnote.so
%attr(755,root,root) %{_libdir}/libopensync1/formats/vtodo.so
