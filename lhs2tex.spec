#% global debug_package %{nil}
#% define _cabal_setup Setup.lhs
%define _no_haddock 1
%define module lhs2tex
Name:           %{module}
Version:        1.18.1
Release:        2
Summary:        Preprocessor for typesetting Haskell sources with LaTeX
Group:          Development/Other
License:        GPLv2+
URL:            https://hackage.haskell.org/package/%{module}
Source0:        http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz

BuildRequires:  ghc, ghc-devel, haskell-macros, haddock
buildrequires:  haskell(regex-compat)
buildrequires:  dblatex
Requires(pre):  ghc
requires(pre):  haskell(regex-compat)

%description
Preprocessor for typesetting Haskell sources with LaTeX

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_compil

%install
%_cabal_install
%_cabal_rpm_gen_deps

%check
%_cabal_check

%files
%defattr(-,root,root,-)
%{_docdir}/%{module}-%{version}
%_cabal_rpm_deps_dir
%{_datadir}/%{module}-%{version}
%{_mandir}/man1/*
%{_bindir}/lhs2TeX


