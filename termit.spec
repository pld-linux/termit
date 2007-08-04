Summary:	TermIt - terminal emulator based on the vte library
Summary(pl.UTF-8):	TermIt - emulator terminala oparty na bibliotece vte
Name:		termit
Version:	1.0.1
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://termit.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	975fc6cbfbe59e81813a98ae03cf7108
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://code.google.com/p/termit/wiki/TermIt
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	pkgconfig
BuildRequires:	vte-devel >= 0.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TermIt - simple terminal emulator based on vte library. Features:
 - tabs
 - bookmarks
 - changing tab name
 - changing font for tabs
 - encodings (all available from GTK+ 2)

Configuration can be changed via $HOME/.termit file (example is
provided).

%description -l pl.UTF-8
TermIt - prosty emulator terminala oparty na bibliotece vte. Zawiera:
 - karty
 - zakładki
 - możliwość zmiany nazw kart
 - możliwość zmiany fontów kart
 - obsługa wszystkich kodowań znaków z GTK+ 2

Konfiguracja może być zmieniana przez plik $HOME/.termit (przykład
znajduje się w dokumentacji).

%prep
%setup -q

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/termit.example
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
