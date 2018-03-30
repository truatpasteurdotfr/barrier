FROM ubuntu:16.04
## 
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install \
build-essential cmake qt5-default \
wget \
libxtst-dev libxinerama-dev libice-dev libxrandr-dev \
libavahi-compat-libdnssd-dev \
libcurl4-openssl-dev \
libssl-dev \
dh-make
#  
RUN wget https://github.com/truatpasteurdotfr/barrier/archive/v2.0.0.tar.gz  && tar xzvf  v2.0.0.tar.gz  
# during the testing period using truatpasteurdotfr/barrier pre-released tarball
# final version should use the https://github.com/debauchee/barrier release versions
RUN cd barrier-2.0.0 && dpkg-buildpackage -us -uc | tee debian.log 
