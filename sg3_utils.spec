Summary:	Utilities and test programs for the Linux sg version 3 device driver
Summary(pl):	Programy narzêdziowe i testowe dla linuksowego sterownika sg w wersji 3
Name:		sg3_utils
Version:	1.05
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.torque.net/sg/p/%{name}-%{version}.tgz
# Source0-md5:	1ec2a247dc347a0e649713e2cecb8fb6
Patch0:		%{name}-make.patch
URL:		http://www.torque.net/sg/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains some utilities and test programs for the Linux
sg (version 3) device driver. This driver is found in the Linux 2.4+
kernels.

%description -l pl
Ten pakiet zawiera trochê programów narzêdziowych i testowych dla
sterownika urz±dzeñ sg w wersji 3. Ten sterownik jest obecny w j±drach
Linuksa 2.4+.

%prep
%setup -q
%patch -p1

%build
%{__make} \
	CC="%{__cc}" \
	LD="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -D_REENTRANT \$(LARGE_FILE_FLAGS)" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	MANDIR=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS README*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
