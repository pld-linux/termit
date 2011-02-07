Summary:	TermIt - terminal emulator based on the vte library, extensible via Lua
Summary(hu.UTF-8):	TermIt - vte könyvtáron alapuló terminál emulátor, Lua nyelven keresztül bővíthető
Summary(pl.UTF-8):	TermIt - emulator terminala oparty na bibliotece vte, rozszerzalny przez Lua
Name:		termit
Version:	2.7.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://github.com/downloads/nonstop/termit/%{name}-%{version}.tar.bz2
# Source0-md5:	e7fbed7a6397a3461a597e9f2e690884
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-language.patch
Patch1:		%{name}-as-needed.patch
URL:		http://wiki.github.com/nonstop/termit/
BuildRequires:	cmake >= 2.6.1
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	lua51-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	vte-devel >= 0.17.1
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
 - beépített Lua
 - xterm-szerű dinamikus ablakcím

A konfiguráció megváltoztatható a $HOME/.config/termit/init.lua fájl
megváltoztatásával (példafájl van a csomagban).

%description -l pl.UTF-8
TermIt - prosty emulator terminala oparty na bibliotece vte. Zawiera:
 - obsługę wielu zakładek
 - przełączanie kodowań
 - obsługę sesji
 - konfigurowalne przypisania klawiszy
 - możliwość rozszerzania przez Lua
 - możliwość dynamicznej zmiany tytułu w stylu xterma

Konfiguracja może być zmieniana przez plik
$HOME/.config/termit/init.lua (przykład znajduje się w dokumentacji).

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%cmake .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog TODO doc/README doc/rc.lua.example doc/lua_api.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
