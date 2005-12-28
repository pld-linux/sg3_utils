Summary:	Utilities and test programs for the Linux sg version 3 device driver
Summary(pl):	Programy narzêdziowe i testowe dla linuksowego sterownika sg w wersji 3
Name:		sg3_utils
Version:	1.19
Release:	1
License:	GPL (utilities), BSD (library)
Group:		Applications/System
Source0:	http://sg.torque.net/sg/p/%{name}-%{version}.tgz
# Source0-md5:	49901944d4663400d178ec5420a9b9a9
Patch0:		%{name}-make.patch
Patch1:		%{name}-llh.patch
URL:		http://sg.torque.net/sg/
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains some utilities and test programs for the Linux
sg (version 3) device driver. This driver is found in the Linux 2.4+
kernels.

%description -l pl
Ten pakiet zawiera trochê programów narzêdziowych i testowych dla
sterownika urz±dzeñ sg w wersji 3. Ten sterownik jest obecny w j±drach
Linuksa 2.4+.

%package devel
Summary:	Header files for sgutils library
Summary(pl):	Pliki nag³ówkowe biblioteki sgutils
License:	BSD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for sgutils library.

%description devel -l pl
Pliki nag³ówkowe biblioteki sgutils.

%package static
Summary:	Static sgutils library
Summary(pl):	Statyczna biblioteka sgutils
License:	BSD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of sgutils library.

%description static -l pl
Statyczna wersja biblioteki sgutils.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	LD="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -D_REENTRANT \$(LARGE_FILE_FLAGS)" \
	LDFLAGS="%{rpmldflags}" \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG COVERAGE CREDITS README*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man8/*.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/scsi/sg_*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
