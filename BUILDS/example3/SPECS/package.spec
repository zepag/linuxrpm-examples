%if 0%{?suse_version}
%define dist .suse%{suse_version}
%endif
%define installationPath /opt/devoxx-rpm
%{!?JAVA_VERSION: %define JAVA_VERSION 1.8.0}
%{!?JAVA_RELEASE: %define JAVA_RELEASE 40}
%{!?JAVA_TM_VERSION: %define JAVA_TM_VERSION 8}
%{!?JAVA_BUILD: %define JAVA_TM_VERSION 26}
%define origin oracle
%define DYNAMIC_LOADER_NAME ld-linux-x86-64.so.2()(64bit)
%define __jar_repack %{nil}

Name: devoxx-ex3-jdk-%{JAVA_VERSION}_%{JAVA_RELEASE}-64bit
Version: 1.0.0	
Release: 1%{?dist}
Summary: a JDK

Group:	Phony
License: (c) Oracle Corporation Binary Code License Agreement

# in order to avoid bogus detected odbc dependencies
AutoReqProv: no

# java-1.5.0-ibm from jpackage.org set Epoch to 1 for unknown reasons,
# and this change was brought into RHEL-4.  java-1.5.0-ibm packages
# also included the epoch in their virtual provides.  This created a
# situation where in-the-wild java-1.5.0-ibm packages provided "java =
# 1:1.5.0".  In RPM terms, "1.6.0 < 1:1.5.0" since 1.6.0 is
# interpreted as 0:1.6.0.  So the "java >= 1.6.0" requirement would be
# satisfied by the 1:1.5.0 packages.  Thus we need to set the epoch in
# JDK package >= 1.6.0 to 1, and packages referring to JDK virtual
# provides >= 1.6.0 must specify the epoch, "java >= 1:1.6.0".
Epoch: 1

Provides: jre-%{JAVA_VERSION}-%{origin} = %{epoch}:%{version}-%{release}
Provides: jre-%{origin} = %{epoch}:%{version}-%{release}
Provides: jre-%{JAVA_VERSION} = %{epoch}:%{version}-%{release}
Provides: jre = %{epoch}:%{JAVA_VERSION}
Provides: java-%{JAVA_VERSION}-%{origin} = %{epoch}:%{version}-%{release}
Provides: java-%{JAVA_VERSION} = %{epoch}:%{version}-%{release}
Provides: java-%{origin} = %{JAVA_VERSION}
Provides: java = %{epoch}:%{JAVA_VERSION}
Provides: jdk-%{JAVA_VERSION}-%{origin} = %{epoch}:%{version}-%{release}
Provides: jdk-%{JAVA_VERSION} = %{epoch}:%{version}-%{release}
Provides: jdk-%{origin} = %{epoch}:%{JAVA_VERSION}
Provides: jdk = %{epoch}:%{JAVA_VERSION}

Requires: %{DYNAMIC_LOADER_NAME}

Source0: jdk-%{JAVA_TM_VERSION}u%{JAVA_RELEASE}-linux-x64.tar.gz


%description
This Package is an example package for Linux Packaging Lab in Devoxx France.
It packages a JDK in a custom path in the filesystem.

# Prep is used to set up the environment for building the rpm package
# Expansion of source tar balls are done in this section
%prep
mkdir -p $RPM_BUILD_DIR/%{installationPath}/jdk64/%{JAVA_VERSION}_%{JAVA_RELEASE}
cd $RPM_BUILD_DIR/%{installationPath}/jdk64/%{JAVA_VERSION}_%{JAVA_RELEASE}
tar xzf %{SOURCE0}

# In this case we're only going to put our files into a directory structure similar to
# the required directory structure after installation
%install
mkdir -p $RPM_BUILD_ROOT%{installationPath}/jdk64/%{JAVA_VERSION}_%{JAVA_RELEASE}/
mv $RPM_BUILD_DIR%{installationPath}/jdk64/%{JAVA_VERSION}_%{JAVA_RELEASE}/jdk%{JAVA_VERSION}_%{JAVA_RELEASE}/* \
   $RPM_BUILD_ROOT%{installationPath}/jdk64/%{JAVA_VERSION}_%{JAVA_RELEASE}/

%files
%defattr(-,root,root,-)
%{installationPath}/jdk64/%{JAVA_VERSION}_%{JAVA_RELEASE}/*

%changelog
* Wed Apr 8 2015 Pierre-Antoine Gregoire <pierre.antoine.gregoire@gmail.com>
 - v1.0.0: First release
