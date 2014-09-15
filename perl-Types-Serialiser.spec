#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Types
%define		pnam	Serialiser
%include	/usr/lib/rpm/macros.perl
Summary:	Types::Serialiser - simple data types for common serialisation formats
Name:		perl-Types-Serialiser
Version:	1.0
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/ML/MLEHMANN/Types-Serialiser-1.0.tar.gz
# Source0-md5:	76460a2bfbc644672499af89192e03fe
URL:		http://search.cpan.org/dist/Types-Serialiser/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{perl_vendorlib}/Types/*.pm
%{perl_vendorlib}/Types/Serialiser
%{_mandir}/man3/*
