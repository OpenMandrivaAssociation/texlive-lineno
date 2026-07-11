%global tl_name lineno
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.9
Release:	%{tl_revision}.1
Summary:	Line numbers on paragraphs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lineno
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lineno.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lineno.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Adds line numbers to selected paragraphs with reference possible through
the LaTeX \ref and \pageref cross reference mechanism. Line numbering
may be extended to footnote lines, using the fnlineno package.

