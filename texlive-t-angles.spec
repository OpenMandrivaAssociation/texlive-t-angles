%global tl_name t-angles
%global tl_revision 71991

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Draw tangles, trees, Hopf algebra operations and other pictures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/t-angles
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/t-angles.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/t-angles.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX2e package for drawing tangles, trees, Hopf algebra operations
and other pictures. It is based on emTeX or TPIC \specials. Therefore,
it can be used with the most popular drivers, including emTeX drivers,
dviwin, xdvi and dvips, and (using some code from ConTeXt) it may also
be used with pdfLaTeX.

