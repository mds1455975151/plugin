#!/bin/bash

handle=$(cat /sys/class/net/eth0/address)
date=`date +%s`
host=docker-agent

echo "[{\
  \"endpoint\"   : \"$host\",\
  \"tags\"       : \"\",\
  \"timestamp\"  : $date,\
  \"metric\"     : \"net.mac\",\
  \"value\"      : \"$handle\",\
  \"counterType\": \"GAUGE\",\
  \"step\"       : 3600}]"

