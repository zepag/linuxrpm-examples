%if 0%{?suse_version}
%define dist .suse%{suse_version}
%endif
%define installationPath /opt/devoxx-rpm
%define javaversion 1.8.0
%define javarelease 40
%define origin oracle
%define DYNAMIC_LOADER_NAME ld-linux-x86-64.so.2()(64bit)
%define __jar_repack %{nil}

Name: devoxx-ex3-jdk-%{javaversion}_%{javarelease}-64bit
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

Provides: jre-%{javaversion}-%{origin} = %{epoch}:%{version}-%{release}
Provides: jre-%{origin} = %{epoch}:%{version}-%{release}
Provides: jre-%{javaversion} = %{epoch}:%{version}-%{release}
Provides: jre = %{epoch}:%{javaversion}
Provides: java-%{javaversion}-%{origin} = %{epoch}:%{version}-%{release}
Provides: java-%{javaversion} = %{epoch}:%{version}-%{release}
Provides: java-%{origin} = %{javaversion}
Provides: java = %{epoch}:%{javaversion}
Provides: jdk-%{javaversion}-%{origin} = %{epoch}:%{version}-%{release}
Provides: jdk-%{javaversion} = %{epoch}:%{version}-%{release}
Provides: jdk-%{origin} = %{epoch}:%{javaversion}
Provides: jdk = %{epoch}:%{javaversion}

Requires: %{DYNAMIC_LOADER_NAME}

Source0: jdk-8u40-linux-x64.tar.gz


%description
This Package is an example package for Linux Packaging Lab in Devoxx France

# Prep is used to set up the environment for building the rpm package
# Expansion of source tar balls are done in this section
%prep
mkdir -p $RPM_BUILD_DIR/%{installationPath}/jdk64/%{javaversion}_%{javarelease}
cd $RPM_BUILD_DIR/%{installationPath}/jdk64/%{javaversion}_%{javarelease}
tar xzf %{SOURCE0}

# In this case we're only going to put our files into a directory structure similar to
# the required directory structure after installation
%install
mkdir -p $RPM_BUILD_ROOT%{installationPath}/jdk64/%{javaversion}_%{javarelease}/
mv $RPM_BUILD_DIR%{installationPath}/jdk64/%{javaversion}_%{javarelease}/jdk1.8.0_40/* \
   $RPM_BUILD_ROOT%{installationPath}/jdk64/%{javaversion}_%{javarelease}/

%files
%defattr(-,root,root,-)
%{installationPath}/jdk64/%{javaversion}_%{javarelease}/*

%changelog
* Wed Apr 8 2015 Pierre-Antoine Gregoire <pierre.antoine.gregoire@gmail.com>
 - v1.0.0: First release
