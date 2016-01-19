%{!?_licensedir: %global license %%doc}

%global modname bcrypt
%global sum     Modern password hashing for your software and your servers

Name:               python-bcrypt
Version:            2.0.0
Release:            3%{?dist}
Summary:            %{sum}

#crypt_blowfish code is in Public domain and all other code in ASL 2.0
License:            ASL 2.0 and Public Domain
URL:                http://pypi.python.org/pypi/bcrypt
Source0:            https://pypi.python.org/packages/source/b/%{modname}/%{modname}-%{version}.tar.gz

Conflicts:         py-bcrypt

BuildRequires:      python2-devel
BuildRequires:      python-setuptools
BuildRequires:      python-cffi
BuildRequires:      python-six
BuildRequires:      python-pytest

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-cffi
BuildRequires:      python3-six
BuildRequires:      python3-pytest

%description
Modern password hashing for your software and your servers


%package -n python2-%{modname}
Summary:            Modern password hashing for your software and your servers
%{?python_provide:%python_provide python2-%{modname}}

Requires:           python-six
Requires:           python-cffi

%description -n python2-%{modname}
Modern password hashing for your software and your servers


%package -n python3-%{modname}
Summary:            Modern password hashing for your software and your servers
%{?python_provide:%python_provide python3-%{modname}}

Requires:           python3-six
Requires:           python3-cffi

%description -n python3-%{modname}
Modern password hashing for your software and your servers


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
* Wed Jan 06 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.0.0-3
- Add conflicts to py-bcrypt since they both provide a bcrypt python module
- Fix macro that were using %%{module} instead of %%{modname}
- In fact the .so files must be executable, so ensure they are such

* Wed Jan 06 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.0.0-2
- Fix the license as the package has some Public Domain files
- Ensure the .so files are not executable

* Tue Jan 05 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.0.0-1
- initial package for Fedora
