#define git 20230823
Name:           hypr
Version:        1.1.4
Release:        3
Summary:        Dynamic tiling window manager
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/Hypr
#Source0:        https://github.com/hyprwm/Hypr/archive/refs/heads/Hypr-main.tar.gz
Source0:        https://github.com/hyprwm/Hypr/archive/%{version}/Hypr-%{version}.tar.gz

Patch0:        fix-hypr-add-install.patch

BuildSystem:   cmake

BuildRequires: pkgconfig
BuildRequires: pkgconfig(gtkmm-3.0)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(xcb-atom)
BuildRequires: pkgconfig(xcb-randr)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(xcb-xinerama)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-icccm)
Requires: xmodmap

%description
Hypr is a dynamic tiling window manager for X

%install -p
install -D -m0755 %{_builddir}/%name-%version/example/%name.desktop %{buildroot}%{_datadir}/xsessions/%name.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/Hypr
%{_datadir}/xsessions/%name.desktop
