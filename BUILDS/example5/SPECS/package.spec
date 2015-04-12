# We don't need to compile python sources as we're just packaging them.
# Moreover version 3.4.6 doesn't seem to compile with Python 2.7, therefore failing
#  in systems where it's the default version.
# The following disables python bytecompile.
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%if 0%{?suse_version}
%define dist .suse%{suse_version}
%endif
%define installationPath /opt/devoxx-rpm
%{!?ZOOKEEPER_VERSION: %define ZOOKEEPER_VERSION 3.4.6}
%{!?GLOBAL_VERSION: %define GLOBAL_VERSION 1.0.0}
%{!?GLOBAL_RELEASE: %define GLOBAL_RELEASE 1%{?dist}}
%define __jar_repack %{nil}
Name: devoxx-ex5-main-package
Version: %{GLOBAL_VERSION}
Release: %{GLOBAL_RELEASE}
Summary: Devoxx Lab Example 5 multi package 
License: No License
Source0: zookeeper-%{ZOOKEEPER_VERSION}.tar.gz
%description
This Package is an example package for Linux Packaging Lab in Devoxx France


%package -n devoxx-ex5-zookeeper-%{ZOOKEEPER_VERSION}
Group: Devoxx/Lab
Summary: Zookeeper %{ZOOKEEPER_VERSION} package
Version: %{GLOBAL_VERSION}
Release: %{GLOBAL_RELEASE}
License: Apache License v2.0
Provides: devoxx-ex5-zookeeper-%{ZOOKEEPER_VERSION}
Provides: zookeeper-%{ZOOKEEPER_VERSION}
Provides: zookeeper
Requires: java-1.8.0-oracle
%description -n devoxx-ex5-zookeeper-%{ZOOKEEPER_VERSION}
This Package is an example package for Linux Packaging Lab in Devoxx France

%package -n devoxx-ex5-zookeeper-doc-%{ZOOKEEPER_VERSION}
Group: Devoxx/Lab
Summary: Zookeeper %{ZOOKEEPER_VERSION} Documentation and examples package
Version: %{GLOBAL_VERSION}
Release: %{GLOBAL_RELEASE}
License: Apache License v2.0
Provides: devoxx-ex5-zookeeper-doc-%{ZOOKEEPER_VERSION}
Provides: zookeeper-%{ZOOKEEPER_VERSION}-doc
Provides: zookeeper-doc
Requires: devoxx-ex5-zookeeper-%{ZOOKEEPER_VERSION}
%description -n devoxx-ex5-zookeeper-doc-%{ZOOKEEPER_VERSION}
This Package is an example package for Linux Packaging Lab in Devoxx France

# Prep is used to set up the environment for building the rpm package
# Expansion of source tar balls are done in this section
%prep
mkdir -p $RPM_BUILD_DIR/%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}
cd $RPM_BUILD_DIR/%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}
tar xzf %{SOURCE0}

# In this case we're only going to put our files into a directory structure similar to
# the required directory structure after installation
%install
mkdir -p $RPM_BUILD_ROOT%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/
mv $RPM_BUILD_DIR%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/zookeeper-%{ZOOKEEPER_VERSION}/zookeeper-*.jar \
   $RPM_BUILD_DIR%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/zookeeper-%{ZOOKEEPER_VERSION}/*.txt \
   $RPM_BUILD_DIR%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/zookeeper-%{ZOOKEEPER_VERSION}/bin \
   $RPM_BUILD_DIR%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/zookeeper-%{ZOOKEEPER_VERSION}/conf \
   $RPM_BUILD_DIR%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/zookeeper-%{ZOOKEEPER_VERSION}/contrib \
   $RPM_BUILD_DIR%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/zookeeper-%{ZOOKEEPER_VERSION}/lib \
   $RPM_BUILD_DIR%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/zookeeper-%{ZOOKEEPER_VERSION}/src \
   $RPM_BUILD_DIR%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/zookeeper-%{ZOOKEEPER_VERSION}/docs \
   $RPM_BUILD_DIR%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/zookeeper-%{ZOOKEEPER_VERSION}/recipes \
   $RPM_BUILD_ROOT%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/

%files -n devoxx-ex5-zookeeper-%{ZOOKEEPER_VERSION}
%defattr(-,root,root,-)
%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/*.txt
%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/zookeeper-*.jar
%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/bin/*
%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/conf/*
%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/contrib/*
%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/lib/*

%files -n devoxx-ex5-zookeeper-doc-%{ZOOKEEPER_VERSION}
%defattr(-,root,root,-)
%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/src/*
%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/docs/*
%{installationPath}/zookeeper/%{ZOOKEEPER_VERSION}/recipes/*

%changelog
* Wed Apr 8 2015 Pierre-Antoine Gregoire <pierre.antoine.gregoire@gmail.com>
 - v1.0.0: First release
