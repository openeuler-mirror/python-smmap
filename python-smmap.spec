%global _empty_manifest_terminate_build 0
Name:		python-smmap
Version:	3.0.4
Release:	1
Summary:	A pure Python implementation of a sliding window memory map manager
License:	BSD
URL:		https://github.com/gitpython-developers/smmap
Source0:	https://files.pythonhosted.org/packages/75/fb/2f594e5364f9c986b2c89eb662fc6067292cb3df2b88ae31c939b9138bb9/smmap-3.0.4.tar.gz
BuildArch:	noarch


%description
%{summary}

%package -n python3-smmap
Summary:	A pure Python implementation of a sliding window memory map manager
Provides:	python-smmap
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-smmap
%{summary}

%package help
Summary:	Development documents and examples for smmap
Provides:	python3-smmap-doc
%description help
%{summary}

%prep
%autosetup -n smmap-3.0.4

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

%files -n python3-smmap -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri Sep 04 2020 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
