%global tl_name pstricks_calcnotes
%global tl_revision 34363

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Use of PSTricks in calculus lecture notes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/pstricks_calcnotes
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks_calcnotes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks_calcnotes.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle shows the construction of PSTricks macros to draw Riemann
sums of an integral and to draw the vector field of an ordinary
differential equation. The results are illustrated in a fragment of
lecture notes.

