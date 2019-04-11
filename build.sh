#!/bin/bash -i

set -e

chown -R root:root /root/rpmbuild
cd /root/rpmbuild/SPECS
rpmbb yq.spec
