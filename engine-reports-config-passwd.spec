Name:		engine-reports-config-passwd
Version:	0.1
Release:	2%{?dist}
Summary:	oVirt Engine Reports Portal User Password Configuration Tool

Group:		Application
License:	GPL
URL:		http://ovirt-china.org
Source0:	engine-reports-config-passwd-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	/bin/bash
Requires:	ovirt-engine-reports

%description
oVirt Engine Reports Portal User Password Configuration Tool.

%prep
%setup -q


%build


%install
rm -rf %{buildroot}
rm -rf .git
mkdir -p %{buildroot}/usr/bin
cp engine-reports-config-passwd %{buildroot}/usr/bin

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%attr(0755,root,root)/usr/bin/engine-reports-config-passwd


%changelog
* Thu Dec  4 2014 MaZhe <mazhe2014@gmail.com> 0.1-2
- Bug fix : Delete non-matched user's file

* Fri Nov 26 2014 MaZhe <mazhe2014@gmail.com> 0.1-1
- Initial package tagging.
