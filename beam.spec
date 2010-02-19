%define name beam
%define snapshot 20091109
%define version 0
%define rel 1
%define release %mkrel 0.%{snapshot}.%{rel}
%define tname %{name}-0.1
%define version 0

Name:           %{name}
Summary: 	Beam tool
Group:		Networking/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Version:        %{version}
Release:        %{release}
License: 	GPL
URL:		http://mds.mandriva.com
Prefix:         %{_prefix}
Source:         %{tname}.tar.bz2
requires:	python lrs

%description
Beam gui

%prep
rm -rf ${RPM_BUILD_ROOT}
%setup -q -n %{tname}

%build

%install
mkdir -p %{buildroot}/opt/%{name}-%{version}
mkdir -p %{buildroot}/%{_sysconfdir}/profile.d
install -m755 $RPM_BUILD_DIR/%{name}-%{version}/*.py %{buildroot}/opt/%{name}-%{version}
cp -avf $RPM_BUILD_DIR/%{name}-%{version}/i18n %{buildroot}/opt/%{name}-%{version}/
cp -avf $RPM_BUILD_DIR/%{name}-%{version}/BeaM* %{buildroot}/opt/%{name}-%{version}/
cp -avf $RPM_BUILD_DIR/%{name}-%{version}/media %{buildroot}/opt/%{name}-%{version}/

cat > %{buildroot}/%{_sysconfdir}/profile.d/beam.sh <<EOF
#!/bin/sh
export PATH=$PATH:/opt/%{name}-%{version}/
EOF

%clean
rm -rf ${RPM_BUILD_ROOT}

%post 
cp -f /proc/partitions /tmp/partitions
mkdir /opt/%{name}-%{version}/lrs-bin
cd /opt/%{name}-%{version}/lrs-bin
for lrsbin in `ls -1 /usr/bin/image_*`
	do ln -sf $lrsbin `basename $lrsbin`
done

ln -sf /usr/bin/autorestore autorestore
ln -sf /usr/bin/autosave autosave
ln -sf /usr/bin/bench bench
ln -sf /usr/bin/ui_newt ui_newt

%postun 
rm -f /tmp/partitions
rm -rf /opt/%{name}-%{version}/lrs-bin

%files
%defattr(-,root,root)
%doc Docs
%attr(755,root,root) /opt/%{name}-%{version}/*.py
/opt/%{name}-%{version}/BeaM*
/opt/%{name}-%{version}/media/*
/opt/%{name}-%{version}/i18n
%attr(755,root,root) %{_sysconfdir}/profile.d/%name.sh

%changelog
