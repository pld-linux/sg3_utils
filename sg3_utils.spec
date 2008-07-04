Summary:	Utilities and test programs for the Linux sg version 3 device driver
Summary(pl.UTF-8):	Programy narzędziowe i testowe dla linuksowego sterownika sg w wersji 3
Name:		sg3_utils
Version:	1.26
Release:	1
License:	GPL (utilities), BSD (library)
Group:		Applications/System
Source0:	http://sg.torque.net/sg/p/%{name}-%{version}.tgz
# Source0-md5:	9a7aa8d954d75dc6c91e066e215867f2
URL:		http://sg.torque.net/sg/
Provides:	sg_utils
Obsoletes:	sg_utils
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
Summary:	Header files for sgutils2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki sgutils2
License:	BSD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for sgutils2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki sgutils2.

%package static
Summary:	Static sgutils2 library
Summary(pl.UTF-8):	Statyczna biblioteka sgutils2
License:	BSD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of sgutils2 library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki sgutils2.

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
%attr(755,root,root) %{_libdir}/libsgutils2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsgutils2.so.2
%{_mandir}/man8/sg*.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsgutils2.so
%{_libdir}/libsgutils2.la
%{_includedir}/scsi/sg_*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libsgutils2.a
