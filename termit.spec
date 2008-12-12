# TODO: change pl description
Summary:	TermIt - terminal emulator based on the vte library
Summary:	TermIt - vte könyvtáron alapuló terminál emulátor
Summary(pl.UTF-8):	TermIt - emulator terminala oparty na bibliotece vte
Name:		termit
Version:	2.1.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://termit.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	ce1dba707a8b803fcb21db4163c50a4a
Source1:	%{name}.desktop
Source2:	%{name}.png
# Patch0:		%{name}-FindLua51.patch
URL:		http://code.google.com/p/termit/wiki/TermIt
BuildRequires:	cmake >= 2.6.1
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	lua51-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	vte-devel >= 0.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TermIt - simple terminal emulator based on vte library. Features:
 - multiple tabs
 - switching encodings
 - sessions
 - configurable keybindings
 - embedded Lua
 - xterm-like dynamic window title

Configuration can be changed via $HOME/.config/termit/init.lua file
(example is provided).

%description -l hu.UTF-8
TermIt - egyszerű, a vte könyvtárra épülő terminál emulátor.
Lehetőségek:
 - több tab
 - kódolás változtatása
 - munkamenetek
 - konfigurálható billentyűkombinációk
 - beépített lua
 - xterm-szerű dinamikus ablakcím

A konfiguráció megváltoztatható a $HOME/.config/termit/init.lua fájl
megváltoztatásával (példafájl van a csomagban).

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
# %patch0 -p1

%build
%{cmake} -D CMAKE_INSTALL_PREFIX:PATH="%{_prefix}" .
# fix --as-needed issue - ref: http://pld-linux.org/DevelopingPLD/AdvancedDeveloping/FixingAsNeeded
%{__perl} -i -p -e 's/((\s-l\S+\s*?)+)((\s\S+\.o\s*?)+)(\s-o termit\s)/\5 \3 \1 /' src/CMakeFiles/termit.dir/link.txt
%{__make} VERBOSE=1

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
%doc ChangeLog TODO doc/README doc/init.lua.example doc/lua_api.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
