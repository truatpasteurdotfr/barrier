Name: barrier
Version: 2.0.0
Summary: Keyboard and mouse sharing solution
Group: Applications/Productivity
URL: https://github.com/debauchee/barrier/
Source: barrier-2.0.0.tar.gz
Vendor: <debauchee.oss@gmail.com>
Packager: Tru Huynh <tru@pasteur.fr>
License: GPLv2
Release: 1%{?dist}

# at least for CentOS-7 and CentOS-6
BuildRequires: cmake3 make gcc gcc-c++ curl-devel  openssl-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: avahi-compat-libdns_sd-devel
BuildREquires: libXtst-devel libXinerama-devel libICE-devel libXrandr-devel

# possible issue here for cmake: on CentOS-7, cmake is cmake 2.x and barrier needs cmake 3.x
# which is available from EPEL as cmake3, that might not be the case for other RPMS based distro

# CXX14
%if 0%{?rhel} == 6
BuildRequires: centos-release-scl-rh
BuildRequires: devtoolset-3-gcc-c++
%endif

%description
Barrier allows you to share one mouse and keyboard between multiple computers.
Work seamlessly across Windows, macOS and Linux.

# fedora 27 not happy without this:
%if 0%{?fedora} == 27
%global debug_package %{nil}
%endif

%prep
#%setup -n %{name}-2.0.0-RC2
%setup -n %{name}-%{version}

%build
echo "export B_BUILD_TYPE=Release"   > build_env.sh
echo "export BARRIER_VERSION_MAJOR=2" >> build_env.sh
echo "export BARRIER_VERSION_MINOR=0" >> build_env.sh
echo "export BARRIER_VERSION_PATCH=0" >> build_env.sh
echo "export BARRIER_VERSION_STAGE=RELEASE" >> build_env.sh
echo "export BARRIER_REVISION=12345678"                     >> build_env.sh
echo 'export B_CMAKE_FLAGS=" -D BARRIER_VERSION_MAJOR=${BARRIER_VERSION_MAJOR} -D BARRIER_VERSION_MINOR=${BARRIER_VERSION_MINOR} -D BARRIER_VERSION_PATCH=${BARRIER_VERSION_PATCH} -D BARRIER_VERSION_STAGE=${BARRIER_VERSION_STAGE} -D BARRIER_REVISION=${BARRIER_REVISION}"'  >> build_env.sh


%if 0%{?rhel} == 6
scl enable devtoolset-3 ./clean_build.sh 
%endif

%if 0%{?rhel} == 7
./clean_build.sh 
%endif

%if 0%{?fedora} 
./clean_build.sh 
%endif


# maybe need a default if/else for non rhel target :P

%install
# no make install, so manual install
%{__mkdir} -p %{buildroot}%{_bindir} %{buildroot}%{_datarootdir}/applications %{buildroot}%{_datarootdir}/icons/hicolor/scalable/apps
%{__install} -t %{buildroot}%{_datarootdir}/applications res/barrier.desktop
%{__install} -t %{buildroot}%{_datarootdir}/icons/hicolor/scalable/apps res/barrier.svg
%{__install} -t %{buildroot}%{_bindir} build/bin/{barrier,barrierc,barriers}

%files
%defattr(755,root,root,-)
%{_bindir}/barrier
%{_bindir}/barrierc
%{_bindir}/barriers
%{_bindir}/syntool
%attr(644,-,-) %{_datarootdir}/applications/barrier.desktop
%attr(644,-,-) %{_datarootdir}/icons/hicolor/scalable/apps/barrier.svg

%changelog
* Sun Mar 25 2018 Tru Huynh <tru@pasteur.fr> - barrier 2.0.0-1
- Initial rpm package for barrier
