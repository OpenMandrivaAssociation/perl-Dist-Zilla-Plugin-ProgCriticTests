%define upstream_name    Dist-Zilla-Plugin-ProgCriticTests
%define upstream_version 1.111750

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Gradually enforce coding standards with Dist::Zilla
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(Dist::Zilla::Plugin::InlineFiles)
BuildRequires:	perl(Dist::Zilla::Role::TextTemplate)
BuildRequires:	perl(Dist::Zilla::Tester)
BuildRequires:	perl(JSON)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Perl::Critic::Progressive)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(YAML::Tiny)
BuildRequires:	perl(autodie)
BuildArch:	noarch

%description
Please see Test::Perl::Critic::Progressive on what exactly it does. For you
it's only important to know that by using this plugin you can avoid the
creep of bad coding practices into your distribution and slowly remove
those that have made their way in already, without being forced to fix
everything at once.

The plugin automatically creates the needed test file and primes it with
all data it needs to know about your dist as well as the options you give.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes README META.yml LICENSE META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*


