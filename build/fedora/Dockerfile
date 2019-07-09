FROM fedora
MAINTAINER \
[Bertrand256 <bertrand256gh@protonmail.com>]
RUN yum update -y \
 && yum group install -y "Development Tools" "Development Libraries" \
 && yum install -y redhat-rpm-config python3-devel libusbx-devel libudev-devel cmake gcc-c++ \
 && yum remove -y gmp-devel \
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
 && set +H \
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
