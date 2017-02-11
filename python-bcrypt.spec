%{!?_licensedir: %global license %%doc}

%global modname bcrypt
%global sum     Modern password hashing for your software and your servers

Name:               python-bcrypt
Version:            3.1.2
Release:            2%{?dist}
Summary:            %{sum}

#crypt_blowfish code is in Public domain and all other code in ASL 2.0
License:            ASL 2.0 and Public Domain and BSD
URL:                http://pypi.python.org/pypi/bcrypt
Source0:            https://files.pythonhosted.org/packages/source/b/%{modname}/%{modname}-%{version}.tar.gz

BuildRequires:      python2-devel
BuildRequires:      python-setuptools
BuildRequires:      python-cffi
BuildRequires:      python-six
BuildRequires:      python-pytest

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-cffi
BuildRequires:      python3-six
#BuildRequires:      python3-pytest

%description
%{sum}.


%package -n python2-%{modname}
Summary:            %{sum}
%{?python_provide:%python_provide python2-%{modname}}

Requires:           python-six
Requires:           python2-cffi
Conflicts:          py-bcrypt

%description -n python2-%{modname}
%{sum}.


%package -n python3-%{modname}
Summary:            %{sum}
%{?python_provide:%python_provide python3-%{modname}}

Requires:           python3-six
Requires:           python3-cffi
Conflicts:          python3-py-bcritp

%description -n python3-%{modname}
%{sum}.


%prep
%autosetup -n %{modname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

# Better safe than sorry
find %{buildroot}%{python2_sitearch} -name '*.so' -exec chmod 755 {} ';'
find %{buildroot}%{python3_sitearch} -name '*.so' -exec chmod 755 {} ';'

#%check
#%{__python2} setup.py test
#%{__python3} setup.py test

%files -n python2-%{modname}
%doc README.rst
%license LICENSE
%{python2_sitearch}/%{modname}/
%{python2_sitearch}/%{modname}-%{version}*

%files -n python3-%{modname}
%doc README.rst
%license LICENSE
%{python3_sitearch}/%{modname}/
%{python3_sitearch}/%{modname}-%{version}*


%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 10 2017 William Moreno <williamjmorenor@gmail.com> - 3.1.2-1
- Update to v3.1.2

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 3.1.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 30 2016 William Moreno <williamjmorenor@gmail.com> - 3.1.0-1
- Update to bugfix release 3.1.0
- Add conflicts for the python3 subpackage

* Thu Jun 30 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 3.0.0-1
- Update to 3.0.0 (Fixes RHBZ#1351377)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.0.0-3
- Add conflicts to py-bcrypt since they both provide a bcrypt python module
- Fix macro that were using %%{module} instead of %%{modname}
- In fact the .so files must be executable, so ensure they are such

* Wed Jan 06 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.0.0-2
- Fix the license as the package has some Public Domain files
- Ensure the .so files are not executable

* Tue Jan 05 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.0.0-1
- initial package for Fedora
