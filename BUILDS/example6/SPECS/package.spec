%if 0%{?suse_version}
%define dist .suse%{suse_version}
%endif

Name: devoxx-ex6-wget
Version: 1.16.3
Release: 1%{?dist}
Summary: A utility for retrieving files using the HTTP or FTP protocols

Group: Application/Internet
License: GPLv3+
URL: http://www.gnu.org/software/wget/
Source0: wget-1.16.3.tar.gz

Provides: wget

%description
GNU Wget is a file retrieval utility which can use either the HTTP or
FTP protocols. Wget features include the ability to work in the
background while you are logged out, recursive retrieval of
directories, file name wildcard matching, remote file timestamp
storage and comparison, use of Rest with FTP servers and Range with
HTTP servers to retrieve files over slow or unstable connections,
support for Proxy servers, and configurability.

%prep
%setup -c

%build
cd $RPM_BUILD_DIR/%{name}-%{version}/wget-%{version}
%configure
make %{?_smp_mflags}

%install
cd $RPM_BUILD_DIR/%{name}-%{version}/wget-%{version}
make install DESTDIR=%{buildroot}
# Avoid conflict with info package
rm %{buildroot}/usr/share/info/dir

%post
/sbin/install-info /usr/share/info/wget.info.gz /usr/share/info/dir || :

%preun
/sbin/install-info --delete /usr/share/info/wget.info.gz /usr/share/info/dir || :

%files
%defattr(-,root,root)
%config /etc/wgetrc
/usr/bin/wget
/usr/share/info/wget.info.gz
/usr/share/locale/*/LC_MESSAGES/wget.mo
/usr/share/man/man1/wget.1.gz

%changelog
* Wed Apr 8 2015 Olivier Robert <bob@fake.com>
 - v1.16.3: living on the edge ;-)
