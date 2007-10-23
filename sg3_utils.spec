Summary:	Utilities and test programs for the Linux sg version 3 device driver
Summary(pl.UTF-8):	Programy narzędziowe i testowe dla linuksowego sterownika sg w wersji 3
Name:		sg3_utils
Version:	1.25
Release:	1
License:	GPL (utilities), BSD (library)
Group:		Applications/System
Source0:	http://sg.torque.net/sg/p/%{name}-%{version}.tgz
# Source0-md5:	9fec4d8f3f6c8b3d2da79fc17cc2d387
URL:		http://sg.torque.net/sg/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains some utilities and test programs for the Linux
sg (version 3) device driver. This driver is found in the Linux 2.4+
kernels.

%description -l pl.UTF-8
Ten pakiet zawiera trochę programów narzędziowych i testowych dla
sterownika urządzeń sg w wersji 3. Ten sterownik jest obecny w jądrach
Linuksa 2.4+.

%package devel
Summary:	Header files for sgutils library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki sgutils
License:	BSD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for sgutils library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki sgutils.

%package static
Summary:	Static sgutils library
Summary(pl.UTF-8):	Statyczna biblioteka sgutils
License:	BSD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of sgutils library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki sgutils.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING COVERAGE CREDITS ChangeLog README README.sg_start
%attr(755,root,root) %{_bindir}/sg*
%attr(755,root,root) %{_libdir}/libsgutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsgutils.so.1
%{_mandir}/man8/sg*.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsgutils.so
%{_libdir}/libsgutils.la
%{_includedir}/scsi/sg_*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libsgutils.a
