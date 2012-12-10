%define name gpppoem
%define version 0.1.1
%define release %mkrel 8

Name: %name
Summary: Monitor your pppoe connection
Version: %{version}
Release: %{release}
License: GPL
Url: http://footprints.altervista.org/index.php
Group: Monitoring
Source0: http://footprints.altervista.org/archivio/gpppoem/%{name}-%{version}.tar.bz2
Source10: gpppoem-16.png
Source11: gpppoem-32.png
Source12: gpppoem-48.png
BuildRequires: automake >= 1.7
Buildrequires: libgnome2-devel >= 2.0
Buildrequires: libgnomeui2-devel >= 2.0

%description
Monitor your pppoe connection. 
It can also monitor your eth0 connection.

%prep
%setup -q -n %name-0.1

%build
export LIBS="-lX11"
autoreconf -vif
%configure2_5x

%install
%makeinstall_std prefix=%buildroot%_prefix

mkdir -p %{buildroot}/{%{_iconsdir},%{_liconsdir},%{_miconsdir}}
cp %SOURCE10 %{buildroot}/%_miconsdir/%name.png
cp %SOURCE11 %{buildroot}/%_iconsdir/%name.png
cp %SOURCE12 %{buildroot}/%_liconsdir/%name.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gpppoem
Comment=Pppoe monitor
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;X-MandrivaLinux-System-Monitoring;
EOF

%files
%defattr(-,root,root,0755)
%{_bindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/pixmaps/%name/gppp.png




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-8mdv2011.0
+ Revision: 619248
- the mass rebuild of 2010.0 packages

* Mon Sep 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-7mdv2010.0
+ Revision: 450311
- fix build
- rebuild for missing binaries

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's error: string list key "Categories" in group "Desktop Entry" does not have a semicolon (";") as trailing character

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 21:16:31 (53674)
- xdg menu
- %%mkrel

* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 21:08:55 (53673)
Import gpppoem

* Sat Jan 29 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.1.1-1mdk
- 0.1.1

