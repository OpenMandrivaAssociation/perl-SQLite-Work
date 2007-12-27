%define module	SQLite-Work
%define name	perl-%{module}
%define version 0.09
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A Perl module to report on and update an SQLite database
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/SQLite/%{module}-%{version}.tar.bz2
BuildRequires:	perl(CGI)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(Getopt::ArgvFile)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Text::NeatTemplate)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}
find . -type f | xargs chmod +w

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README TODO *.cgi
%{perl_vendorlib}/SQLite
%{_mandir}/*/*
%{_bindir}/*

