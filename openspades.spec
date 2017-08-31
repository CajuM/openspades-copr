%global debug_package %{nil}

Name: openspades
Version: 0.1.1c
Release: 1%{?dist}
Summary: Compatible client of Ace of Spades 0.75

License: GPLv3
URL: http://openspades.yvt.jp/
Source0: https://github.com/yvt/openspades/archive/v0.1.1c.tar.gz
Source1: openspades-getcontent
Patch0: no-nonfree.patch

BuildRequires: cmake
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: glew-devel
BuildRequires: libcurl-devel
BuildRequires: zlib-devel
BuildRequires: freetype-devel
BuildRequires: opusfile-devel
BuildRequires: ImageMagick

Requires: SDL2
Requires: SDL2_image
Requires: libGLEW
Requires: libcurl
Requires: freetype
Requires: opusfile
Requires: wget

%description
OpenSpades is a clone of Ace of Spades 0.75, which is a free online first-person shooter created by Ben Aksoy, featuring fully destructible terrain and plenty of game modes (including the well-known Capture the Flag) created by the community.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
cmake . \
	-DCMAKE_INSTALL_PREFIX=/usr \
	-DCMAKE_BUILD_TYPE=Release \
	-DOPENSPADES_RESDIR=/usr/share/openspades/Resources \
	-DOPENSPADES_INSTALL_RESOURCES=share/openspades/Resources \
	-DOPENSPADES_INSTALL_BINARY=bin

make %{?_smp_mflags}


%install
%make_install
install -m 0644 Sources/json/LICENSE %{buildroot}/usr/share/doc/openspades/LICENSE.json.txt
install -m 0644 Sources/ENet/LICENSE %{buildroot}/usr/share/doc/openspades/LICENSE.ENet.txt
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/openspades-getcontent


%check


%files
/usr/share/menu/openspades
/usr/share/icons/hicolor/96x96/apps/openspades.png
/usr/share/icons/hicolor/256x256/apps/openspades.png
/usr/share/icons/hicolor/16x16/apps/openspades.png
/usr/share/icons/hicolor/128x128/apps/openspades.png
/usr/share/icons/hicolor/48x48/apps/openspades.png
/usr/share/icons/hicolor/64x64/apps/openspades.png
/usr/share/icons/hicolor/24x24/apps/openspades.png
/usr/share/icons/hicolor/32x32/apps/openspades.png
/usr/share/applications/openspades.desktop
%dir /usr/share/openspades
%dir /usr/share/openspades/Resources
%ghost /usr/share/openspades/Resources/font-unifont.pak
/usr/share/openspades/Resources/pak999-References.pak
%ghost /usr/share/openspades/Resources/pak000-Nonfree.pak
/usr/share/openspades/Resources/pak005-Models.pak
/usr/share/openspades/Resources/PackageInfo.json
/usr/share/openspades/Resources/pak002-Base.pak
/usr/share/openspades/Resources/pak010-BaseSkin.pak
/usr/share/openspades/Resources/pak050-Locales.pak
%dir /usr/share/doc/openspades
%doc /usr/share/doc/openspades/README.md
%doc /usr/share/doc/openspades/AUTHORS
%doc /usr/share/doc/openspades/changelog.gz
%license /usr/share/doc/openspades/copyright
%license /usr/share/doc/openspades/LICENSE
%license /usr/share/doc/openspades/LICENSE.json.txt
%license /usr/share/doc/openspades/LICENSE.ENet.txt
/usr/share/pixmaps/openspades.xpm
/usr/share/man/man6/openspades.6.gz
/usr/bin/openspades
/usr/bin/openspades-getcontent


%changelog
* Thu Nov 02 2017 Mihai-Drosi Caju <ddan.dcaju@gmail.com> 0.1.1c-1
- Initial commit (ddan.dcaju@gmail.com)



