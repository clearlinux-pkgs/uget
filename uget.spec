#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : uget
Version  : 2.2.3.1
Release  : 4
URL      : https://sourceforge.net/projects/urlget/files/uget%20%28stable%29/2.2.3/uget-2.2.3-1.tar.gz
Source0  : https://sourceforge.net/projects/urlget/files/uget%20%28stable%29/2.2.3/uget-2.2.3-1.tar.gz
Summary  : GTK+ download manager featuring download classification and HTML import
Group    : Development/Tools
License  : LGPL-2.1
Requires: uget-bin = %{version}-%{release}
Requires: uget-data = %{version}-%{release}
Requires: uget-license = %{version}-%{release}
Requires: uget-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : nghttp2-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(appindicator3-0.1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libnotify)

%description
uGet 2.2.3: (2020-01-01)
1. add parser for YouTube recently changed field.
uGet 2.2.2: (2019-05-20)
1. use quicksort to sort downloads.
2. backup torrent and metalink files.
3. curl plug-in: handle duplicate files with double extensions.

%package bin
Summary: bin components for the uget package.
Group: Binaries
Requires: uget-data = %{version}-%{release}
Requires: uget-license = %{version}-%{release}

%description bin
bin components for the uget package.


%package data
Summary: data components for the uget package.
Group: Data

%description data
data components for the uget package.


%package license
Summary: license components for the uget package.
Group: Default

%description license
license components for the uget package.


%package locales
Summary: locales components for the uget package.
Group: Default

%description locales
locales components for the uget package.


%prep
%setup -q -n uget-2.2.3
cd %{_builddir}/uget-2.2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1578160786
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1578160786
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/uget
cp %{_builddir}/uget-2.2.3/COPYING %{buildroot}/usr/share/package-licenses/uget/e60c2e780886f95df9c9ee36992b8edabec00bcc
%make_install
%find_lang uget

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/uget-gtk
/usr/bin/uget-gtk-1to2

%files data
%defattr(-,root,root,-)
/usr/share/applications/uget-gtk.desktop
/usr/share/icons/hicolor/128x128/apps/uget-icon.png
/usr/share/icons/hicolor/16x16/apps/uget-icon.png
/usr/share/icons/hicolor/16x16/apps/uget-tray-default.png
/usr/share/icons/hicolor/16x16/apps/uget-tray-downloading.png
/usr/share/icons/hicolor/16x16/apps/uget-tray-error.png
/usr/share/icons/hicolor/22x22/apps/uget-icon.png
/usr/share/icons/hicolor/22x22/apps/uget-tray-default.png
/usr/share/icons/hicolor/22x22/apps/uget-tray-downloading.png
/usr/share/icons/hicolor/22x22/apps/uget-tray-error.png
/usr/share/icons/hicolor/24x24/apps/uget-icon.png
/usr/share/icons/hicolor/24x24/apps/uget-tray-default.png
/usr/share/icons/hicolor/24x24/apps/uget-tray-downloading.png
/usr/share/icons/hicolor/24x24/apps/uget-tray-error.png
/usr/share/icons/hicolor/32x32/apps/uget-icon.png
/usr/share/icons/hicolor/32x32/apps/uget-tray-default.png
/usr/share/icons/hicolor/32x32/apps/uget-tray-downloading.png
/usr/share/icons/hicolor/32x32/apps/uget-tray-error.png
/usr/share/icons/hicolor/48x48/apps/uget-icon.png
/usr/share/icons/hicolor/48x48/apps/uget-tray-default.png
/usr/share/icons/hicolor/48x48/apps/uget-tray-downloading.png
/usr/share/icons/hicolor/48x48/apps/uget-tray-error.png
/usr/share/icons/hicolor/64x64/apps/uget-icon.png
/usr/share/icons/hicolor/96x96/apps/uget-icon.png
/usr/share/icons/hicolor/scalable/apps/uget-icon.svg
/usr/share/pixmaps/uget/logo.png
/usr/share/sounds/uget/notification.wav

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/uget/e60c2e780886f95df9c9ee36992b8edabec00bcc

%files locales -f uget.lang
%defattr(-,root,root,-)

