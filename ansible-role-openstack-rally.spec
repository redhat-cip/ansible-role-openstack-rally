Name:       ansible-role-openstack-rally
Version:    0.0.VERS
Release:    1%{?dist}
Summary:    ansible-role-openstack-rally
License:    ASL 2.0
URL:        https://github.com/redhat-cip/ansible-role-openstack-rally
Source0:    ansible-role-openstack-rally-%{version}.tar.gz

BuildArch:  noarch
Requires:   ansible

%description
An Ansible role to run Rally OpenStack test suite

%prep
%setup -qc


%build

%install
mkdir -p %{buildroot}%{_datadir}/dci/roles/openstack-rally
chmod 755 %{buildroot}%{_datadir}/dci/roles/openstack-rally

cp -r meta %{buildroot}%{_datadir}/dci/roles/openstack-rally
cp -r tasks %{buildroot}%{_datadir}/dci/roles/openstack-rally
cp -r defaults %{buildroot}%{_datadir}/dci/roles/openstack-rally
cp -r vars %{buildroot}%{_datadir}/dci/roles/openstack-rally


%files
%doc README.md
%license LICENSE
%{_datadir}/dci/roles/openstack-rally


%changelog
* Wed Apr 26 2017 Yanis Guenane <yguenane@redhat.com> - 0.0.1-1
- Initial release
