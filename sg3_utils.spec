Summary:	Utilities and test programs for the Linux sg version 3 device driver
Summary(pl.UTF-8):	Programy narzędziowe i testowe dla linuksowego sterownika sg w wersji 3
Name:		sg3_utils
Version:	1.35
Release:	1
License:	GPL (utilities), BSD (library)
Group:		Applications/System
Source0:	http://sg.danny.cz/sg/p/%{name}-%{version}.tar.xz
# Source0-md5:	01600b51611388c65b6954d99197d529
URL:		http://sg.danny.cz/sg/sg3_utils.html
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Provides:	sg_utils
Obsoletes:	scsiutils
Obsoletes:	sg_utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

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

install scripts/scsi_* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BSD_LICENSE COPYING COVERAGE CREDITS ChangeLog README README.sg_start TODO
%attr(755,root,root) %{_bindir}/scsi_*
%attr(755,root,root) %{_bindir}/sg_*
%attr(755,root,root) %{_bindir}/sginfo
%attr(755,root,root) %{_bindir}/sgm_dd
%attr(755,root,root) %{_bindir}/sgp_dd
%attr(755,root,root) %{_libdir}/libsgutils2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsgutils2.so.2
%{_mandir}/man8/scsi_*.8*
%{_mandir}/man8/sg3_utils.8*
%{_mandir}/man8/sg_*.8*
%{_mandir}/man8/sginfo.8*
%{_mandir}/man8/sgm_dd.8*
%{_mandir}/man8/sgp_dd.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsgutils2.so
%{_libdir}/libsgutils2.la
%{_includedir}/scsi/sg_*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libsgutils2.a
