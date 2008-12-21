
%define		svnrev 1407

Summary:	Tool for communicating over JTAG
Name:		urjtag
Version:	0.9
Release:	0.%{svnrev}.1
License:	GPL v2
Group:		Applications
Source0:	%{name}-%{svnrev}.tar.bz2
# Source0-md5:	d45cef438a688c18a8a767fffcec3c03
Patch0:		%{name}-fix-as_needed.patch
URL:		http://urjtag.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex >= 2.5.33
BuildRequires:	gettext-devel
BuildRequires:	libusb-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UrJTAG aims to create an enhanced, modern tool for communicating over
JTAG with flash chips, CPUs, and many more.

%prep
%setup -q -n %{name}-%{svnrev}
%patch0 -p1
%{__sed} '/po\/Makefile\.in/d' -i configure.ac

%build
%{__gettextize}
%{__aclocal} -I m4
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS doc/UrJTAG.txt doc/README.ejtag doc/howto_add_support_for_more_flash.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
