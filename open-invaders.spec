Summary:	Clone of Space Invaders game
Summary(pl.UTF-8):	Klon gry Space Invaders
Name:		open-invaders
Version:	0.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.jamyskis.net/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	51cbdbc8f0cbba203557489f06de3e8d
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Patch0:		%{name}-useless_files.patch
URL:		http://www.jamyskis.net/invaders.php
BuildRequires:	allegro-devel >= 4.2.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dumb-devel >= 0.9.3
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
open-invaders is a GPL'd clone of Space Invaders game, written in C++
using the Allegro library.

%description -l pl.UTF-8
open-invaders jest klonem gry Space Invaders opartym na licencji GPL,
napisanym w C++ z użyciem biblioteki Allegro.

%prep
%setup -q
%patch -P0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
