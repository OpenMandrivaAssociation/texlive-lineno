Name:		texlive-lineno
Version:	61719
Release:	1
Summary:	Line numbers on paragraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lineno
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lineno.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lineno.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lineno.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Adds line numbers to selected paragraphs with reference
possible through the LaTeX \ref and \pageref cross reference
mechanism. Line numbering may be extended to footnote lines,
using the fnlineno package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lineno/ednmath0.sty
%{_texmfdistdir}/tex/latex/lineno/edtable.sty
%{_texmfdistdir}/tex/latex/lineno/fnlineno.sty
%{_texmfdistdir}/tex/latex/lineno/lineno.sty
%{_texmfdistdir}/tex/latex/lineno/vplref.sty
%doc %{_texmfdistdir}/doc/latex/lineno/CHANGEs.txt
%doc %{_texmfdistdir}/doc/latex/lineno/COPYING.txt
%doc %{_texmfdistdir}/doc/latex/lineno/README
%doc %{_texmfdistdir}/doc/latex/lineno/README.txt
%doc %{_texmfdistdir}/doc/latex/lineno/SRCFILEs.txt
%doc %{_texmfdistdir}/doc/latex/lineno/fnlineno.pdf
%doc %{_texmfdistdir}/doc/latex/lineno/lineno.pdf
%doc %{_texmfdistdir}/doc/latex/lineno/lnosuppl.pdf
%doc %{_texmfdistdir}/doc/latex/lineno/ulineno.pdf
#- source
%doc %{_texmfdistdir}/source/latex/lineno/fnlineno.tex
%doc %{_texmfdistdir}/source/latex/lineno/lineno.tex
%doc %{_texmfdistdir}/source/latex/lineno/lnosuppl.tex
%doc %{_texmfdistdir}/source/latex/lineno/ulineno.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
