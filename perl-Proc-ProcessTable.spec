#
# Conditional build:
%bcond_with	tests	# do perform "make test" (requires mounted /proc)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Proc
%define		pnam	ProcessTable
Summary:	Proc::ProcessTable - Perl interface to the UNIX process table
Summary(pl.UTF-8):	Proc::ProcessTable - interfejs perlowy do uniksowej tabeli procesów
Name:		perl-Proc-ProcessTable
Version:	0.48
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Proc/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ddc2c67cd1184ddb0ba1f84e89b90e2a
Patch0:		format.patch
URL:		http://search.cpan.org/dist/Proc-ProcessTable/
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

%description -l pl.UTF-8
Ten moduł to pierwsza próba udostępnienia spójnego interfejsu do
informacji dotyczących uniksowej (i może z innych wielozadaniowych
systemów operacyjnych) tabeli procesów. Impuls do stworzenia tego
pojawił się wraz z frustracją autora przy analizie wyjścia poleceń ps
z różnych systemów w celu sprawdzenia, czy określone procesy działają
na różnych maszynach w dużym zestawie różnych Uniksów. Format wyjścia
ps był różny na każdym systemie, a czasem zmieniał się wraz z nową
wersją systemu. Poza tym uruchamianie procesu ps z Perla lub skryptu
powłoki i analiza jego wyjścia nie były zbyt wydajnym ani estetycznym
sposobem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%{perl_vendorarch}/auto/Proc/ProcessTable/Process
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_mandir}/man3/*
