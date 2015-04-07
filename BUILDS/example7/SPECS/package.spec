%if 0%{?suse_version}
%define dist .suse%{suse_version}
%endif
%define installationPath /opt/devoxx-rpm/

Name: devoxx-ex1
Version: 1.0.0	
Release: 1%{?dist}
Summary: a basic package adding a file in a known place and creating a link

Group:	Phony
License: NoLicense
Source0: foobar.txt

%description
This Package is an example package for Linux Packaging Lab in Devoxx France

%install
mkdir -p $RPM_BUILD_ROOT%{installationPath}/ex1/
cp %{SOURCE0} $RPM_BUILD_ROOT%{installationPath}/ex1/foobar.txt

%files
%defattr(-,root,root)
%attr(644,root,root) %{installationPath}/ex1/foobar.txt

%changelog
* Wed Apr 8 2015 Pierre-Antoine Gregoire <pierre.antoine.gregoire@gmail.com>
 - v1.0.0: First release
