%define		qtver		4.7.1
%define		kdever		4.5.5

Summary:	DirectShow backend for Phonon
Summary(pl.UTF-8):	Wtyczka DirectShow dla Phonona
Name:		phonon-backend-directshow
Version:	4.4.4
Release:	0.1
License:	LGPL 2.1
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/phonon/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	5d1da5927a5b37f47d0616a10aa9b9fa
#URL:		http://
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	phonon-devel >= 4.4.4
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Provides:	qt4-phonon-backend = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DirectShow backend for Phonon.

%description -l pl.UTF-8
Wtyczka DirectShow dla Phonona.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_directshow.so
%{_datadir}/kde4/services/phononbackends/directshow.desktop
