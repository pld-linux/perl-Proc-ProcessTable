#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Proc
%define	pnam	ProcessTable
Summary:	Proc::ProcessTable - Perl interface to the unix process table
Summary(pl):	Proc::ProcessTable - perlowy interfejs do uniksowej tabeli procesów
Name:		perl-Proc-ProcessTable
Version:	0.35
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Storable
BuildRequires:	perl-modules
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a first crack at providing a consistent interface to
Unix (and maybe other multitasking OS's) process table information.
The impetus for this came about with my frustration at having to parse
the output of various systems' ps commands to check whether specific
processes were running on different boxes at a larged mixed Unix site.
The output format of ps was different on each OS, and sometimes
changed with each new release of an OS. Also, running a ps subprocess
from within a perl or shell script and parsing the output was not a
very efficient or aesthetic way to do things.

%description -l pl
Ten modu³ to pierwsza próba udostêpnienia spójnego interfejsu do
informacji dotycz±cych uniksowej (i mo¿e z innych wielozadaniowych
systemów operacyjnych) tabeli procesów. Impuls do stworzenia tego
pojawi³ siê wraz z frustracj± autora przy analizie wyj¶cia poleceñ ps
z ró¿nych systemów w celu sprawdzenia, czy okre¶lone procesy dzia³aj±
na ró¿nych maszynach w du¿ym zestawie ró¿nych uniksów. Format wyj¶cia
ps by³ ró¿ny na ka¿dym systemie, a czasem zmienia³ siê wraz z now±
wersj± systemu. Poza tym uruchamianie procesu ps z Perla lub skryptu
pow³oki i analiza jego wyj¶cia nie by³y zbyt wydajnym ani estetycznym
sposobem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.linux PORTING Changes TODO
%{perl_sitearch}/%{pdir}/*.pm
%{perl_sitearch}/%{pdir}/%{pnam}
%dir %{perl_sitearch}/auto/%{pdir}/%{pnam}
%attr(755,root,root) %{perl_sitearch}/auto/%{pdir}/%{pnam}/*.so
%{perl_sitearch}/auto/%{pdir}/%{pnam}/*.bs
%{perl_sitearch}/auto/%{pdir}/%{pnam}/Process
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
