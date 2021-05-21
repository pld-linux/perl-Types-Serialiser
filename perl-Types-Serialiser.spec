#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Types
%define		pnam	Serialiser
Summary:	Types::Serialiser - simple data types for common serialisation formats
Summary(pl.UTF-8):	Types::Serialiser - proste typy danych do popularnych formatów serializacji
Name:		perl-Types-Serialiser
Version:	1.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/ML/MLEHMANN/Types-Serialiser-%{version}.tar.gz
# Source0-md5:	4839af5f3fcbacc3945b0e6f3dc9a018
URL:		https://metacpan.org/release/Types-Serialiser
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-common-sense
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides some extra datatypes that are used by common
serialisation formats such as JSON or CBOR. The idea is to have a
repository of simple/small constants and containers that can be shared
by different implementations so they become interoperable between each
other.

%description -l pl.UTF-8
Ten moduł dostarcza kilka dodatkowych typów danych, używanych w
popularnych formatach, takich jak JSON czy CBOR. Pomysł polega na tym,
żeby było wspólne repozytorium prostych/małych stałych i kontenerów,
które można współdzielić między różnymi implementacjami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Types
%{perl_vendorlib}/Types/Serialiser.pm
%{perl_vendorlib}/Types/Serialiser
%{_mandir}/man3/Types::Serialiser*.3pm*
