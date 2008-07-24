%define module	Unicode-UTF8simple
%define name	perl-%{module}
%define version 1.06
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Conversions to/from UTF8 from/to charactersets
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/G/GU/GUS/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:	perl-Unicode-Map
Buildrequires:	perl-Unicode-Map8
Buildrequires:	perl-Jcode
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This utf-8 converter is written in plain perl and works with hopefully
any perl 5 version. It was mainly written because more recent modules
such as Encode do not work under older Perl 5.0 installations.

%prep
%setup -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Unicode
%{_mandir}/*/*


