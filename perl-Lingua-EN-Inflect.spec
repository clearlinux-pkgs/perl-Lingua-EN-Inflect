#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Lingua-EN-Inflect
Version  : 1.905
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Lingua-EN-Inflect-1.905.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Lingua-EN-Inflect-1.905.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblingua-en-inflect-perl/liblingua-en-inflect-perl_1.903-1.debian.tar.xz
Summary  : 'Convert singular to plural. Select "a" or "an".'
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Lingua-EN-Inflect-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Lingua::EN::Inflect version 1.905
The exportable subroutines of Lingua::EN::Inflect provide plural
inflections and "a"/"an" selection for English words.

%package dev
Summary: dev components for the perl-Lingua-EN-Inflect package.
Group: Development
Provides: perl-Lingua-EN-Inflect-devel = %{version}-%{release}
Requires: perl-Lingua-EN-Inflect = %{version}-%{release}

%description dev
dev components for the perl-Lingua-EN-Inflect package.


%package perl
Summary: perl components for the perl-Lingua-EN-Inflect package.
Group: Default
Requires: perl-Lingua-EN-Inflect = %{version}-%{release}

%description perl
perl components for the perl-Lingua-EN-Inflect package.


%prep
%setup -q -n Lingua-EN-Inflect-1.905
cd %{_builddir}
tar xf %{_sourcedir}/liblingua-en-inflect-perl_1.903-1.debian.tar.xz
cd %{_builddir}/Lingua-EN-Inflect-1.905
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Lingua-EN-Inflect-1.905/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Lingua::EN::Inflect.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
