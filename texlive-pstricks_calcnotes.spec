# revision 33361
# category Package
# catalog-ctan /info/pstricks_calcnotes
# catalog-date 2014-04-03 16:06:38 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-pstricks_calcnotes
Epoch:		1
Version:	1.2
Release:	3
Summary:	Use of PStricks in calculus lecture notes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/pstricks_calcnotes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks_calcnotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks_calcnotes.doc.tar.xz
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
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/Convert_PstricksCode_To_Pdf/Readme.txt
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/Convert_PstricksCode_To_Pdf/convert.tex
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/Convert_PstricksCode_To_Pdf/test.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig13.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig14.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig1a.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig1b.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig1c.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig2a.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig2b.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig3.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig4.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig5.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig6.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig7.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig8.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig9.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/ThreeAppsPDF.tex
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/b6of1.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/b6of2.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/b6of3.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/b6of4.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vecb1.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vecb2.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vecb3.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vecb4.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vecb5.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vecb6.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/ThreeAppsPS.tex
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/b6of1.eps
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/b6of2.eps
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/b6of3.eps
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/b6of4.eps
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vecb1.eps
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vecb2.eps
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vecb3.eps
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vecb4.eps
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vecb5.eps
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vecb6.eps
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/README
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/ThreeAppsPDF.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
