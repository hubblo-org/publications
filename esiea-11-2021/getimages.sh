#!/bin/bash

QCOW_IMAGE="myimage.qcow2.gz"
OVA_IMAGE="proxmox.ova"
MD5SUM="https://raw.githubusercontent.com/hubblo-org/publications/master/esiea-11-2021/md5sum"

curl ${MD5SUM} -s -o md5sum
curl https://raw.githubusercontent.com/hubblo-org/publications/master/esiea-11-2021/mydomain.xml -s -o mydomain.xml

curl https://sync.nce.re/index.php/s/2EqzdgqxNA3pWn3/download -# -o ${QCOW_IMAGE}
if [ $? -eq 0 ]; then
  res=$(md5sum ${QCOW_IMAGE}); grep ${res} md5sum && gunzip ${QCOW_IMAGE} && echo "${QCOW_IMAGE} downloaded, sane, then gunzipped."
else
  echo "Download of ${QCOW_IMAGE} failed !"
fi
curl https://sync.nce.re/index.php/s/Ap9eWykmnC49Cnx/download -# -o ${OVA_IMAGE}
if [ $? -eq 0 ]; then
  res=$(md5sum ${OVA_IMAGE}); grep ${res} md5sum && echo "${OVA_IMAGE}, sane, downloaded."
else
  echo "Download of ${OVA_IMAGE} failed !"
fi
