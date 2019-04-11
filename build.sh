#!/bin/bash -i

set -e

chown -R root:root /root/rpmbuild
cd /root/rpmbuild/SPECS
spectool -R -g yq.spec
rpmbb yq.spec
