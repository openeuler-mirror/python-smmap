%global _empty_manifest_terminate_build 0
Name:		python-smmap
Version:	0.8.5
Release:	1
Summary:	A pure git implementation of a sliding window memory map manager
License:	BSD
URL:		https://github.com/gitpython-developers/smmap
Source0:	https://files.pythonhosted.org/packages/b9/4d/849ec5427a58981538739212e43f6019da27995388afb2416eb891e5daad/smmap-0.8.5.tar.gz
BuildArch:	noarch
%description
When reading from many possibly large files in a fashion similar to random access, it is usually the fastest and most efficient to use memory maps.

Although memory maps have many advantages, they represent a very limited system resource as every map uses one file descriptor, whose amount is limited per process. On 32 bit systems, the amount of memory you can have mapped at a åtime is naturally limited to theoretical 4GB of memory, which may not be enough for some applications.

**The documentation can be found here**: http://smmap.readthedocs.org

%package -n python2-smmap
Summary:	A pure git implementation of a sliding window memory map manager
Provides:	python2-smmap
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
BuildRequires:	python2-pbr
%description -n python2-smmap
When reading from many possibly large files in a fashion similar to random access, it is usually the fastest and most efficient to use memory maps.

Although memory maps have many advantages, they represent a very limited system resource as every map uses one file descriptor, whose amount is limited per process. On 32 bit systems, the amount of memory you can have mapped at a åtime is naturally limited to theoretical 4GB of memory, which may not be enough for some applications.

**The documentation can be found here**: http://smmap.readthedocs.org

%package help
Summary:	Development documents and examples for smmap
Provides:	python2-smmap-doc
%description help
When reading from many possibly large files in a fashion similar to random access, it is usually the fastest and most efficient to use memory maps.

Although memory maps have many advantages, they represent a very limited system resource as every map uses one file descriptor, whose amount is limited per process. On 32 bit systems, the amount of memory you can have mapped at a åtime is naturally limited to theoretical 4GB of memory, which may not be enough for some applications.

**The documentation can be found here**: http://smmap.readthedocs.org

%prep
%autosetup -n smmap-0.8.5

%build
%py2_build

%install
%py2_install
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

%files -n python2-smmap -f filelist.lst
%dir %{python2_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Tue Jun 01 2021 OpenStack_SIG <openstack@openeuler.org>
- Package Spec generated
