%global _empty_manifest_terminate_build 0
Name:           python-smmap
Version:        3.0.5
Release:        2
Summary:        A pure Python implementation of a sliding window memory map manager
License:        BSD
URL:            https://github.com/gitpython-developers/smmap
Source0:        https://files.pythonhosted.org/packages/2b/6f/d48bbed5aa971943759f4ede3f12dca40aa7faa44f22bad483de86780508/smmap-3.0.5.tar.gz
BuildArch:      noarch

%description
A pure Python implementation of a sliding window memory map manager

%package -n python3-smmap
Summary:        A pure Python implementation of a sliding window memory map manager
Provides:       python-smmap
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel

%description -n python3-smmap
A pure Python implementation of a sliding window memory map manager

%package help
Summary:        A pure Python implementation of a sliding window memory map manager
Provides:       python3-smmap-doc

%description help
A pure Python implementation of a sliding window memory map manager

%prep
%autosetup -n smmap-%{version}

%build
%py3_build

%install
%py3_install

install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
    find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
    find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
    find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
    find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%check
%{__python3} setup.py test

%files -n python3-smmap -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri Feb 11 2022 wangxiyuan <wangxiyuan1007@gmail.com> - 3.0.5-2
- Remove nosecover BuildRequire since the required nose library has been removed from openEuler already.

* Fri Aug 06 2021 OpenStack_SIG <openstack@openeuler.org> - 3.0.5-1
- Upgrade version to 3.0.5

* Fri Sep 04 2020 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
