%global tl_name ppt-slides
%global tl_revision 79345

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8.0
Release:	%{tl_revision}.1
Summary:	Good-looking slide decks a la PowerPoint (PPT)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ppt-slides
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ppt-slides.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ppt-slides.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ppt-slides.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(anyfontsize)
Requires:	texlive(changepage)
Requires:	texlive(crumbs)
Requires:	texlive(enumitem)
Requires:	texlive(fontsize)
Requires:	texlive(hardwrap)
Requires:	texlive(href-ul)
Requires:	texlive(ifoddpage)
Requires:	texlive(lastpage)
Requires:	texlive(listings)
Requires:	texlive(pagecolor)
Requires:	texlive(pgf)
Requires:	texlive(pgfopts)
Requires:	texlive(qrcode)
Requires:	texlive(seqsplit)
Requires:	texlive(soul)
Requires:	texlive(textpos)
Requires:	texlive(tikzpagenodes)
Requires:	texlive(titling)
Requires:	texlive(varwidth)
Requires:	texlive(xcolor)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package helps you create slide decks as good-looking as with
PowerPointtm, but more precise, uniform, and visually strict. Check this
series of lectures fully designed with the use of this package.

