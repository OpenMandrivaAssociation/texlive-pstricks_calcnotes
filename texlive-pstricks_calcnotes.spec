# revision 31821
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-pstricks_calcnotes
Version:	20131010
Release:	1
Summary:	TeXLive pstricks_calcnotes package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks_calcnotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks_calcnotes.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive pstricks_calcnotes package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/Convert_PstricksCode_To_Pdf/Readme.txt
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/Convert_PstricksCode_To_Pdf/convert.tex
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/Convert_PstricksCode_To_Pdf/test.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig1-1.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig1-2.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig1-3.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig2-1.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig2-2.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig3.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig4.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig5.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig6.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig7.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig8.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/Fig9.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/NewVecFld_PDF.tex
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vec1.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vec2.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vec3.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vec4.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vec5.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/vec6.pdf
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/NewVecFld_PS.tex
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vec1.eps
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vec2.eps
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vec3.eps
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vec4.eps
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vec5.eps
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/vec6.eps
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/README
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/Two_Apps_Remarks.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
