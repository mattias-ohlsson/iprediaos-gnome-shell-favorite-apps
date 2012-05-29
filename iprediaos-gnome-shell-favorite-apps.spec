Name:		iprediaos-gnome-shell-favorite-apps
Version:	1
Release:	1%{?dist}
Summary:	Override Gnome Shell favorite apps

Group:		User Interface/Desktops
License:	GPLv2+
URL:		http://www.ipredia.org
Source0:	iprediaos-gnome-shell-favorite-apps-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
Requires:	gnome-shell
BuildArch:      noarch


%description
Provides Gnome Shell favorite apps for IprediaOS.

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.override


%changelog
* Tue May 29 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 1.1
- Initial package
