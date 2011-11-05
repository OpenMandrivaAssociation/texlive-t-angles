# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/t-angles
# catalog-date 2007-03-12 14:32:12 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-t-angles
Version:	20070312
Release:	1
Summary:	Draw tangles, trees, Hopf algebra operations and other pictures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/t-angles
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/t-angles.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/t-angles.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A LaTeX2e package for drawing tangles, trees, Hopf algebra
operations and other pictures. It is based on emTeX or TPIC
\special's. Therefore, it can be used with the most popular
drivers, including emTeX drivers, dviwin, xdvi and dvips, and
(using some code from ConTeXt) it may also be used with
PDFLaTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/t-angles/t-angles.sty
%doc %{_texmfdistdir}/doc/latex/t-angles/README
%doc %{_texmfdistdir}/doc/latex/t-angles/t-manual.pdf
%doc %{_texmfdistdir}/doc/latex/t-angles/t-manual.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
