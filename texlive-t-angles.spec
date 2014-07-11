# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/t-angles
# catalog-date 2007-03-12 14:32:12 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-t-angles
Version:	20070312
Release:	8
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070312-2
+ Revision: 756510
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070312-1
+ Revision: 719654
- texlive-t-angles
- texlive-t-angles
- texlive-t-angles
- texlive-t-angles

