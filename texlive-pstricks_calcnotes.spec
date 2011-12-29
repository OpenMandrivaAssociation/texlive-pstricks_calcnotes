# revision 18816
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-pstricks_calcnotes
Version:	20111104
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
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/Convert_PstricsCode_To_Pdf/Readme.txt
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/Convert_PstricsCode_To_Pdf/convert.tex
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/Convert_PstricsCode_To_Pdf/test.pdf
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
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Pdf_Output/TwoApps_Pdf.tex
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/For_Ps_Output/TwoApps_Ps.tex
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/README
%doc %{_texmfdistdir}/doc/latex/pstricks_calcnotes/two_apps.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
