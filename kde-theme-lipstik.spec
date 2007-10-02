
%define         _name lipstik

Summary:	KDE theme - %{_name}
Summary(pl.UTF-8):	Motyw KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	2.2.3
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/CONTENT/content-files/18223-%{_name}-%{version}.tar.gz
# Source0-md5:	809112598947796145d19a01f138345c
URL:		http://www.kde-look.org/content/show.php?content=18223
BuildRequires:	autoconf
BuildRequires:	unsermake
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} is a theme based on the plastik style, Lipstik is a purified
style with many options to tune your desktop look.

%description -l pl.UTF-8
%{_name} to motyw oparty na Plastiku. Jest jednak oczyszczony i
posiada wiele opcji umożliwiających precyzyjne ustawienie wyglądu
pulpitu.

%package -n kde-style-%{_name}
Summary:	KDE Style - %{_name}
Summary(pl.UTF-8):	Styl dla KDE - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-style-%{_name}
KDE style - %{_name}.

%description -n kde-style-%{_name} -l pl.UTF-8
Styl dla KDE - %{_name}

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for %{_name} theme
Summary(pl.UTF-8):	Zestaw kolorów dla stylu %{_name}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
A color scheme for %{_name} theme.

%description -n kde-colorscheme-%{_name} -l pl.UTF-8
Zestaw kolorów dla stylu %{_name}.

%prep
%setup -q -n %{_name}-%{version}

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{configure}
%{__make}

%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-theme-%{_name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kstyle_*.so
%{_libdir}/kde3/kstyle_*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_libdir}/kde3/plugins/styles/*.la
%{_datadir}/apps/kstyle/themes/*.themerc

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/lipstik*.kcsrc
