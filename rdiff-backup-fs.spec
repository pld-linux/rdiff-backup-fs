Summary:	Filesystem in userspace for rdiff-backup repositories
Summary(hu.UTF-8):	Fájlrendszer userspace-en belül rdiff-backup tárolókhoz
Name:		rdiff-backup-fs
Version:	1.0.0
Release:	0.1
License:	GPL v3
Group:		Applications/Archiving
Source0:	http://rdiff-backup-fs.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	c59fb6796ff4a70e0759fbc79b52db07
URL:		http://code.google.com/p/rdiff-backup-fs/
BuildRequires:	libfuse-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesystem in userspace for rdiff-backup repositories.

%description -l hu.UTF-8
Fájlrendszer userspace-en belül rdiff-backup tárolókhoz.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
