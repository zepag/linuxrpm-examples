%{!?PRODUCT_VERSION: %define PRODUCT_VERSION 5.2.7}
%define installationPath /opt/devoxx-rpm


Name: devoxx-ex4-unrar-%{PRODUCT_VERSION}
Version: 1.0.0	
Release: 1%{?dist}
Summary: UnRAR built from sources

Group:	Phony
License: RAR and WinRAR END USER LICENSE AGREEMENT (EULA)

Provides: unrar = %{PRODUCT_VERSION}

Source0: unrarsrc-%{PRODUCT_VERSION}.tar.gz


%description
This Package is an example package for Linux Packaging Lab in Devoxx France

# Prep is used to set up the environment for building the rpm package
# Expansion of source tar balls are done in this section
%prep
%setup -c 

%build
cd $RPM_BUILD_DIR/%{name}-%{version}/unrar
make %{?_smp_mflags} 

# In this case we're only going to put our files into a directory structure similar to
# the required directory structure after installation
%install
mkdir -p %{buildroot}%{installationPath}/unrar/%{PRODUCT_VERSION}/
cd $RPM_BUILD_DIR/%{name}-%{version}/unrar
install -v -m755 unrar %{buildroot}%{installationPath}/unrar/%{PRODUCT_VERSION}/

%files
%defattr(-,root,root,-)
%attr(755,root, root) %{installationPath}/unrar/%{PRODUCT_VERSION}/

%changelog
* Wed Apr 8 2015 Pierre-Antoine Gregoire <pierre.antoine.gregoire@gmail.com>
 - v1.0.0: First release
