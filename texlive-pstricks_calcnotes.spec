Name:		texlive-pstricks_calcnotes
Epoch:		1
Version:	34363
Release:	2
Summary:	Use of PStricks in calculus lecture notes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/pstricks_calcnotes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks_calcnotes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks_calcnotes.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The bundle shows the construction of PStricks macros to draw
Riemann sums of an integral and to draw the vector field of an
ordinary differential equation. The results are illustrated in
a fragment of lecture notes.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
