Name:		texlive-ppt-slides
Version:	71155
Release:	1
Summary:	Good-looking slide decks a la PowerPoint (PPT)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ppt-slides
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ppt-slides.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ppt-slides.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package helps you create slide decks as good-looking
as with PowerPointtm, but more precise, uniform, and visually
strict. Check this series of lectures fully designed with the
use of this package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ppt-slides
%doc %{_texmfdistdir}/doc/latex/ppt-slides

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
