%define installationPath /opt/devoxx-rpm/

Name: devoxx-ex2
Version: 1.0.0	
Release: 1%{?dist}
Summary: a package with a dependency

Group:	Phony
License: NoLicense
Requires: devoxx-ex1

%description
This Package is an example package for Linux Packaging Lab in Devoxx France

%install

%files

%changelog
* Wed Apr 8 2015 Pierre-Antoine Gregoire <pierre.antoine.gregoire@gmail.com>
 - v1.0.0: First release
