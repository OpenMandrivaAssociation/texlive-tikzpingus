Name:		texlive-tikzpingus
Version:	72990
Release:	1
Summary:	Penguins with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tikzpingus
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpingus.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpingus.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
tikzpingus is a package similar to tikzducks but with penguins
and a vast set of gadgets and extras (capable of changing the
wing-positions, body-types, and more).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikzpingus
%{_texmfdistdir}/makeindex/tikzpingus
%doc %{_texmfdistdir}/doc/latex/tikzpingus

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
