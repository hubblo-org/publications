#!/bin/bash

FILENAME="myimage.qcow2.gz"

curl https://sync.nce.re/index.php/s/2EqzdgqxNA3pWn3/download -# -o ${FILENAME}
if [ $? -eq 0 ]; then
  gunzip ${FILENAME}
else
  echo "Download failed !"
fi
