Summary:	OpenSync vFormat Plugin
Name:		libopensync-plugin-vformat
Version:	0.30
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/libopensync-vformat-%{version}.tar.bz2?format=raw
# Source0-md5:	f7b6144ed7ceaf50b1d0eec21401f19d
URL:		http://www.opensync.org/
BuildRequires:	glib2-devel >= 1:2.4
BuildRequires:	libopensync-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	scons
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

Ten pakiet zawiera wtyczkę vformat dla szkieletu OpenSync.

%prep
%setup -q -n libopensync-vformat-%{version}

%build
%scons \
	prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
%scons install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/opensync/formats/*.so
