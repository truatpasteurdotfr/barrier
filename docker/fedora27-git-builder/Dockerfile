FROM fedora:27

RUN yum -y update && yum -y upgrade
RUN yum -y install git cmake3 make qt5-qtbase-devel gcc \
 avahi-compat-libdns_sd-devel gcc-c++ curl-devel \
 openssl-devel \
 libXtst-devel libXinerama-devel libICE-devel libXrandr-devel \
 rpm-build

#RUN git clone https://github.com/debauchee/barrier/
RUN git clone https://github.com/truatpasteurdotfr/barrier/
RUN cd barrier && ./build_rpm.sh | tee clean_build.log 
