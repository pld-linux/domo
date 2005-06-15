Summary:	A music organising database application
Summary(pl):	Organizator aplikacji muzycznych
Name:		domo
Version:	2.4
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/domo/%{name}-%{version}.tar.gz
# Source0-md5:	9a1b631b81b3b84145cfe4d336310622
Patch0:		%{name}-%{version}_include.patch
URL:		http://domo.sf.net
BuildRequires:	qt-devel >= 3.3.4
BuildRequires:	qt-plugin-mysql >= 3.3.4
BuildRequires:	taglib-devel >= 1.2
BuildRequires:	libmusicbrainz >= 2.0
BuildRequires:	libmad-devel
BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Domo is a music organizer which indexes digital audio sources,
extracts all information and inserts everything into a relational
database. The database can then be queried, exported and compared with
other digital audio sources. Musicbrainz support is also available for
the looking up of Audio CDs or for identifying unknown tracks based on
their TRM audio fingerprint.

%description -l pl
Domo jest organizerem muzyki, który indeksuje cyfrowe ¼ród³a d¼wiêku,
wydobywa ca³± informacjê oraz umieszcz± j± w bazie danych.

%prep
%setup -q
%patch0 -p1

%build

# Create the language files
%{_bindir}/lrelease domo.pro

# Create the makefile
%{_bindir}/qmake domo.pro

# Compile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install
	DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf %{buildroot}

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/domo
%dir %{_sysconfdir}/domo
%dir %{_sysconfdir}/domo/resources/
%{_sysconfdir}/domo/resources/*.txt
%dir %{_sysconfdir}/domo/images/
%{_sysconfdir}/domo/images/*.png
%dir %{_sysconfdir}/domo/languages/
%{_sysconfdir}/domo/languages/*.qm
%dir %{_sysconfdir}/domo/doc
%dir %{_sysconfdir}/domo/doc/*

%doc INSTALL RELEASE README CHANGELOG
