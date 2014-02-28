Summary:	Monitor your pppoe connection
Name:		gpppoem
Version:	0.1.1
Release:	9
License:	GPLv2+
Group:		Monitoring
Url:		http://footprints.altervista.org/index.php
Source0:	http://footprints.altervista.org/archivio/%{name}/%{name}-%{version}.tar.bz2
Source10:	gpppoem-16.png
Source11:	gpppoem-32.png
Source12:	gpppoem-48.png
BuildRequires:	pkgconfig(libgnome-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)

%description
Monitor your pppoe connection. It can also monitor your eth0 connection.

%files
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/pixmaps/%{name}/gppp.png

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-0.1

find . -name "Makefile*" -o -name "*.m4" -o -name "configure*" |xargs sed -i -e 's,configure.in,configure.ac,g'

%build
export LIBS="-lX11"
autoreconf -vif
%configure2_5x

%install
%makeinstall_std prefix=%{buildroot}%{_prefix}

mkdir -p %{buildroot}/{%{_iconsdir},%{_liconsdir},%{_miconsdir}}
cp %{SOURCE10} %{buildroot}%{_miconsdir}/%{name}.png
cp %{SOURCE11} %{buildroot}%{_iconsdir}/%{name}.png
cp %{SOURCE12} %{buildroot}%{_liconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
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

