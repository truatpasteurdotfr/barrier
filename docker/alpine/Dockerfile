FROM alpine:3.7

RUN apk update && apk upgrade
RUN apk add git cmake make qt5-qtbase-dev gcc \
 avahi-dev g++ curl-dev \
 libressl-dev libxinerama-dev libice-dev libxrandr-dev  \
 libx11-dev libxtst-dev 


RUN git clone https://github.com/debauchee/barrier/
# pending a PR since which is not installed by default on the CentOS-7 docker image
# `type cmake3 >> /dev/null` && B_CMAKE=`type cmake3 | cut -d ' ' -f 3` instead of B_CMAKE=`which cmake3 2>/dev/null`
RUN apk add  which 
# pending patch for libressl from synergy-core cf barrier/issue/12
ADD alpine.patch /
RUN (cd barrier && patch -p1  -i ../alpine.patch)
RUN cd barrier && ./clean_build.sh | tee clean_build.log && tar czvf build.tgz build clean_build.log
