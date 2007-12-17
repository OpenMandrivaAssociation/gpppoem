%define name gpppoem
%define version 0.1.1
%define release %mkrel 2

Name: %name
Summary: Monitor your pppoe connection
Version: %{version}
Release: %{release}
License: GPL
Url: http://footprints.altervista.org/index.php
Group: Monitoring
Source: http://footprints.altervista.org/archivio/gpppoem/%{name}-%{version}.tar.bz2
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
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
%setup -q -n %name-0.1

%build
%configure

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std prefix=%buildroot%_prefix

mkdir -p %{buildroot}/{%{_iconsdir},%{_liconsdir},%{_miconsdir}}
cp %SOURCE10 %{buildroot}/%_miconsdir/%name.png
cp %SOURCE11 %{buildroot}/%_iconsdir/%name.png
cp %SOURCE12 %{buildroot}/%_liconsdir/%name.png
mkdir -p %{buildroot}/%{_menudir}
cat << EOF > %{buildroot}/%{_menudir}/%{name}
?package(%name):command="%{_bindir}/gpppoem" icon="%name.png" \
                needs="X11" section="Applications/Monitoring" \
 title="Gpppoem" longtitle="Pppoe monitor" \
 xdg="true"
EOF

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

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files -f %name.lang
%defattr(-,root,root,0755)
%{_bindir}/*
%_menudir/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/pixmaps/%name/gppp.png


