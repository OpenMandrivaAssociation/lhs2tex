
Summary:	A preprocessor to generate LaTeX code from literate Haskell sources
Name:		lhs2tex
Version:	1.12
Release:	%mkrel 4
Source0:	http://people.cs.uu.nl/andres/lhs2tex/%{name}-%{version}.tar.bz2
License: 	GPL
Group:		Development/Other
Url:		http://www.cs.uu.nl/~andres/lhs2tex/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ghc
BuildRequires:	tetex

%description
lhs2TeX is a preprocessor to generate LaTeX code from literate Haskell sources.

lhs2TeX includes the following features:

 * Different styles to process your source file: for instance, "tt" style uses
a monospaced font for the code while still allowing you to highlight keywords
etc, whereas "poly" style uses proportional fonts for identifiers, handles
indentation nicely, is able to replace binary operators by mathematical symbols
and take care of complex horizontal alignments.
 * Formatting directives, which let you customize the way certain tokens in the
source code should appear in the processed output.
 * A liberal parser that can handle most of the language extensions; you don't
have to restrict yourself to Haskell 98.
 * Preprocessor-style conditionals that allow you to generate different
versions of a document from a single source file (for instance, a paper and a
presentation).
 * Active documents: you can use Haskell to generate parts of the document
(useful for papers on Haskell).
 * A manual explaining all the important aspects of lhs2TeX.


%prep
%setup -q

%build

%configure
%make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/usr/local/share/texmf $RPM_BUILD_ROOT/%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
%doc Examples/ LICENSE RELEASE doc/Guide2.pdf 

