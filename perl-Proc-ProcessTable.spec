#
# Conditional build:
%bcond_with	tests	# do perform "make test" (requires mounted /proc)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Proc
%define		pnam	ProcessTable
Summary:	Proc::ProcessTable - Perl interface to the UNIX process table
Summary(pl):	Proc::ProcessTable - interfejs perlowy do uniksowej tabeli procesów
Name:		perl-Proc-ProcessTable
Version:	0.39
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c153cf906e8b71ac847fa5c3e79970de
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a first crack at providing a consistent interface to
Unix (and maybe other multitasking OS's) process table information.
The impetus for this came about with my frustration at having to parse
the output of various systems' ps commands to check whether specific
processes were running on different boxes at a larged mixed UNIX site.
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
na ró¿nych maszynach w du¿ym zestawie ró¿nych Uniksów. Format wyj¶cia
ps by³ ró¿ny na ka¿dym systemie, a czasem zmienia³ siê wraz z now±
wersj± systemu. Poza tym uruchamianie procesu ps z Perla lub skryptu
pow³oki i analiza jego wyj¶cia nie by³y zbyt wydajnym ani estetycznym
sposobem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install example.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.linux PORTING Changes TODO
%dir %{perl_vendorarch}/Proc
%{perl_vendorarch}/Proc/*.pm
%{perl_vendorarch}/Proc/ProcessTable
%dir %{perl_vendorarch}/auto/Proc
%dir %{perl_vendorarch}/auto/Proc/ProcessTable
%attr(755,root,root) %{perl_vendorarch}/auto/Proc/ProcessTable/*.so
%{perl_vendorarch}/auto/Proc/ProcessTable/*.bs
%{perl_vendorarch}/auto/Proc/ProcessTable/Process
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_mandir}/man3/*
