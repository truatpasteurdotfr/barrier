FROM centos:centos6

RUN yum -y update && yum -y upgrade
RUN yum -y install epel-release
RUN yum -y install cmake3 make qt5-qtbase-devel gcc \
 avahi-compat-libdns_sd-devel gcc-c++ curl-devel \
 openssl-devel \
 libXtst-devel libXinerama-devel libICE-devel libXrandr-devel \
 wget rpm-build 

# c6 g++ is not CXX14
RUN yum -y install centos-release-scl-rh
# devtoolset-3 is enough but one can use devtoolset-N
RUN yum -y install devtoolset-3-gcc-c++.x86_64

# during the testing period using truatpasteurdotfr/barrier pre-released tarball
# final version should use the https://github.com/debauchee/barrier release versions
#RUN wget https://github.com/truatpasteurdotfr/barrier/archive/v2.0.0-RC2.tar.gz  -O barrier-2.0.0-RC2.tar.gz  && scl enable devtoolset-3 'rpmbuild -ta barrier-2.0.0-RC2.tar.gz' | tee rpmbuild.log
RUN mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS} && \
wget https://github.com/debauchee/barrier/archive/v2.0.0.tar.gz -O ~/rpmbuild/SOURCES/barrier-2.0.0.tar.gz && \
wget https://raw.githubusercontent.com/truatpasteurdotfr/barrier/master/barrier.spec -O ~/rpmbuild/SPECS/barrier.spec  && \
scl enable devtoolset-3 'rpmbuild -ba ~/rpmbuild/SPECS/barrier.spec' | tee rpmbuild.log

#RUN wget https://github.com/truatpasteurdotfr/barrier/archive/v2.0.0-RC2.tar.gz  -O barrier-2.0.0-RC2.tar.gz  && rpmbuild -ta barrier-2.0.0-RC2.tar.gz  | tee rpmbuild.log
