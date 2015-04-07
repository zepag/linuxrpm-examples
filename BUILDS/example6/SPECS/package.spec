%if 0%{?suse_version}
%define dist .suse%{suse_version}
%endif

Name: wget
Version: 1.16.3
Release: 1%{?dist}
Summary: A utility for retrieving files using the HTTP or FTP protocols

Group: Application/Internet
License: GPLv3+
URL: http://www.gnu.org/software/wget/
Source0: wget-1.16.3.tar.gz

%description
GNU Wget is a file retrieval utility which can use either the HTTP or
FTP protocols. Wget features include the ability to work in the
background while you are logged out, recursive retrieval of
directories, file name wildcard matching, remote file timestamp
storage and comparison, use of Rest with FTP servers and Range with
HTTP servers to retrieve files over slow or unstable connections,
support for Proxy servers, and configurability.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
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
#/usr/share/info/dir
/usr/share/info/wget.info.gz
/usr/share/locale/be/LC_MESSAGES/wget.mo
/usr/share/locale/bg/LC_MESSAGES/wget.mo
/usr/share/locale/ca/LC_MESSAGES/wget.mo
/usr/share/locale/cs/LC_MESSAGES/wget.mo
/usr/share/locale/da/LC_MESSAGES/wget.mo
/usr/share/locale/de/LC_MESSAGES/wget.mo
/usr/share/locale/el/LC_MESSAGES/wget.mo
/usr/share/locale/en_GB/LC_MESSAGES/wget.mo
/usr/share/locale/eo/LC_MESSAGES/wget.mo
/usr/share/locale/es/LC_MESSAGES/wget.mo
/usr/share/locale/et/LC_MESSAGES/wget.mo
/usr/share/locale/eu/LC_MESSAGES/wget.mo
/usr/share/locale/fi/LC_MESSAGES/wget.mo
/usr/share/locale/fr/LC_MESSAGES/wget.mo
/usr/share/locale/ga/LC_MESSAGES/wget.mo
/usr/share/locale/gl/LC_MESSAGES/wget.mo
/usr/share/locale/he/LC_MESSAGES/wget.mo
/usr/share/locale/hr/LC_MESSAGES/wget.mo
/usr/share/locale/hu/LC_MESSAGES/wget.mo
/usr/share/locale/id/LC_MESSAGES/wget.mo
/usr/share/locale/it/LC_MESSAGES/wget.mo
/usr/share/locale/ja/LC_MESSAGES/wget.mo
/usr/share/locale/lt/LC_MESSAGES/wget.mo
/usr/share/locale/nb/LC_MESSAGES/wget.mo
/usr/share/locale/nl/LC_MESSAGES/wget.mo
/usr/share/locale/pl/LC_MESSAGES/wget.mo
/usr/share/locale/pt/LC_MESSAGES/wget.mo
/usr/share/locale/pt_BR/LC_MESSAGES/wget.mo
/usr/share/locale/ro/LC_MESSAGES/wget.mo
/usr/share/locale/ru/LC_MESSAGES/wget.mo
/usr/share/locale/sk/LC_MESSAGES/wget.mo
/usr/share/locale/sl/LC_MESSAGES/wget.mo
/usr/share/locale/sr/LC_MESSAGES/wget.mo
/usr/share/locale/sv/LC_MESSAGES/wget.mo
/usr/share/locale/tr/LC_MESSAGES/wget.mo
/usr/share/locale/uk/LC_MESSAGES/wget.mo
/usr/share/locale/vi/LC_MESSAGES/wget.mo
/usr/share/locale/zh_CN/LC_MESSAGES/wget.mo
/usr/share/locale/zh_TW/LC_MESSAGES/wget.mo
/usr/share/man/man1/wget.1.gz

%changelog
* Wed Apr 8 2015 Olivier Robert <bob@fake.com>
 - v1.16.3: living on the edge ;-)
