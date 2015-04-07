%if 0%{?suse_version}
%define dist .suse%{suse_version}
%endif

Name: devoxx-ex2
Version: 1.0.0	
Release: 1%{?dist}
Summary: a package with a dependency

Group:	Devoxx/Lab
License: NoLicense
Requires: devoxx-ex1

%description
This Package is an example package for Linux Packaging Lab in Devoxx France.
It provides nothing by itself, but has a dependency, i.e. Requires another package.

%install

%files

%changelog
* Wed Apr 8 2015 Pierre-Antoine Gregoire <pierre.antoine.gregoire@gmail.com>
 - v1.0.0: First release
