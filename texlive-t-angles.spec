Name:		texlive-t-angles
Version:	15878
Release:	2
Summary:	Draw tangles, trees, Hopf algebra operations and other pictures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/t-angles
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/t-angles.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/t-angles.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX2e package for drawing tangles, trees, Hopf algebra
operations and other pictures. It is based on emTeX or TPIC
\special's. Therefore, it can be used with the most popular
drivers, including emTeX drivers, dviwin, xdvi and dvips, and
(using some code from ConTeXt) it may also be used with
PDFLaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/t-angles/t-angles.sty
%doc %{_texmfdistdir}/doc/latex/t-angles/README
%doc %{_texmfdistdir}/doc/latex/t-angles/t-manual.pdf
%doc %{_texmfdistdir}/doc/latex/t-angles/t-manual.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
