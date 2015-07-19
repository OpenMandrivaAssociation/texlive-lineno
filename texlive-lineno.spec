# revision 21442
# category Package
# catalog-ctan /macros/latex/contrib/lineno
# catalog-date 2011-02-16 17:09:51 +0100
# catalog-license lppl
# catalog-version 4.41
Name:		texlive-lineno
Version:	4.41
Release:	10
Summary:	Line numbers on paragraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lineno
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lineno.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lineno.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lineno.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.41-2
+ Revision: 753312
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.41-1
+ Revision: 718862
- texlive-lineno
- texlive-lineno
- texlive-lineno
- texlive-lineno

