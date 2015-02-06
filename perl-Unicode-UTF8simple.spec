%define upstream_name	 Unicode-UTF8simple
%define upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Conversions to/from UTF8 from/to charactersets
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/G/GU/GUS/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-Unicode-Map
BuildRequires:	perl-Unicode-Map8
BuildRequires:	perl-Jcode
BuildArch:	noarch

%description
This utf-8 converter is written in plain perl and works with hopefully
any perl 5 version. It was mainly written because more recent modules
such as Encode do not work under older Perl 5.0 installations.

%prep
%setup -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Unicode
%{_mandir}/*/*


%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.60.0-1mdv2010.0
+ Revision: 401992
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.06-4mdv2009.0
+ Revision: 258709
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.06-3mdv2009.0
+ Revision: 246669
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.06-1mdv2008.1
+ Revision: 136364
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 03 2007 Stefan van der Eijk <stefan@mandriva.org> 1.06-1mdv2007.0
+ Revision: 103815
- Import perl-Unicode-UTF8simple

* Fri Dec 02 2005 Stefan an der Eijk <stefan@eijk.nu> 1.06-1mdk
- initial package

