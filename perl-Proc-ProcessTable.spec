#
# Conditional build:
%bcond_with	tests	# do perform "make test" (requires mounted /proc)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Proc
%define		pnam	ProcessTable
Summary:	Proc::ProcessTable - Perl interface to the UNIX process table
Summary(pl):	Proc::ProcessTable - interfejs perlowy do uniksowej tabeli proces�w
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
Ten modu� to pierwsza pr�ba udost�pnienia sp�jnego interfejsu do
informacji dotycz�cych uniksowej (i mo�e z innych wielozadaniowych
system�w operacyjnych) tabeli proces�w. Impuls do stworzenia tego
pojawi� si� wraz z frustracj� autora przy analizie wyj�cia polece� ps
z r�nych system�w w celu sprawdzenia, czy okre�lone procesy dzia�aj�
na r�nych maszynach w du�ym zestawie r�nych Uniks�w. Format wyj�cia
ps by� r�ny na ka�dym systemie, a czasem zmienia� si� wraz z now�
wersj� systemu. Poza tym uruchamianie procesu ps z Perla lub skryptu
pow�oki i analiza jego wyj�cia nie by�y zbyt wydajnym ani estetycznym
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
