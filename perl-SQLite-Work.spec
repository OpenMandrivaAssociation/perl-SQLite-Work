%define upstream_name	 SQLite-Work
%define upstream_version 0.1002

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A Perl module to report on and update an SQLite database
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SQLite/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(Getopt::ArgvFile)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Text::NeatTemplate)
BuildArch:	noarch

%description
This generates HTML (and non-HTML) reports from an SQLite database, taking care
of the query-building and the report formatting. This also has methods for
adding and updating the database.

The SQLite::Work::CGI module has extra methods which deal with CGI using the
CGI module; the included "show.cgi" and "edit.cgi" are demonstration CGI
scripts which use the SQLite::Work::CGI module.

The sqlreport script uses SQLite::Work to generate reports from the
command-line.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find . -type f | xargs chmod +w

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README TODO *.cgi
%{perl_vendorlib}/SQLite
%{_mandir}/*/*
%{_bindir}/*

%changelog
* Tue Jul 07 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.100.200-1mdv2010.0
+ Revision: 393241
- update to 0.1002
- using %%perl_convert_version
- fixed license field

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.09-5mdv2009.0
+ Revision: 258382
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.09-4mdv2009.0
+ Revision: 246426
- rebuild

* Thu Dec 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-2mdv2008.1
+ Revision: 138307
- fix build dependencies
- fix build

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Thauvin <nanardon@mandriva.org>
    - 0.09


* Thu Feb 23 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-2mdk
- Fix BuildRequires
- make rpmbuildupdate friendly

* Fri Feb 17 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.04-1mdk
- Initial Mandriva release.

