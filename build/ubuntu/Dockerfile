FROM ubuntu:17.10
MAINTAINER \
[Bertrand256 <bertrand256gh@protonmail.com>]
RUN apt-get update \
 && apt-get -y upgrade \
 && apt-get -y install libudev-dev libusb-1.0-0-dev libfox-1.6-dev autotools-dev autoconf automake libtool libpython3-all-dev python3.6-dev python3-pip git cmake \
 && pip3 install virtualenv \
 && cd ~ \
 && mkdir fixmt \
 && cd fixmt \
 && virtualenv -p python3 venv \
 && . venv/bin/activate \
 && pip install --upgrade setuptools \
 && git clone https://github.com/Bertrand256/fix-masternode-tool \
 && cd fix-masternode-tool/ \
 && pip install -r requirements.txt \
 && cd ~/fixmt \
 && echo "#!/bin/sh" | tee build-fixmt.sh \
 && echo "cd ~/fixmt" | tee -a build-fixmt.sh \
 && echo ". venv/bin/activate" | tee -a build-fixmt.sh \
 && echo "cd fix-masternode-tool" | tee -a build-fixmt.sh \
 && echo "git fetch --all" | tee -a build-fixmt.sh \
 && echo "git reset --hard origin/master" | tee -a build-fixmt.sh \
 && echo "pip install -r requirements.txt" | tee -a build-fixmt.sh \
 && echo "pyinstaller --distpath=../dist/linux --workpath=../dist/linux/build fix_masternode_tool.spec" | tee -a build-fixmt.sh \
 && echo "cd .." | tee -a build-fixmt.sh \
 && chmod +x build-fixmt.sh

CMD ~/fixmt/build-fixmt.sh
