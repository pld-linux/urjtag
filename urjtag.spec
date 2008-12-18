#
Summary:	Tool for communicating over JTAG
Name:		urjtag
Version:	0.9
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/urjtag/%{name}-%{version}.tar.bz2
# Source0-md5:	684fc54354e1e600102244c0e7bf6643
Patch0:		%{name}-fix-as_needed.patch
URL:		http://urjtag.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libusb-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UrJTAG aims to create an enhanced, modern tool for communicating over
JTAG with flash chips, CPUs, and many more.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS doc/UrJTAG.txt doc/README.ejtag doc/howto_add_support_for_more_flash.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
