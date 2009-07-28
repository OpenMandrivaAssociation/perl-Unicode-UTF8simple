%define upstream_name	 Unicode-UTF8simple
%define upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Conversions to/from UTF8 from/to charactersets
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/G/GU/GUS/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:	perl-Unicode-Map
Buildrequires:	perl-Unicode-Map8
Buildrequires:	perl-Jcode
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This utf-8 converter is written in plain perl and works with hopefully
any perl 5 version. It was mainly written because more recent modules
such as Encode do not work under older Perl 5.0 installations.

%prep
%setup -n %{upstream_name}-%{upstream_version}

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
