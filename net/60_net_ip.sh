#!/bin/bash

handle=$(ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1)
date=`date +%s`
host=docker-agent

echo "[{\
  \"endpoint\"   : \"$host\",\
  \"tags\"       : \"\",\
  \"timestamp\"  : $date,\
  \"metric\"     : \"net.ip\",\
  \"value\"      : \"$handle\",\
  \"counterType\": \"GAUGE\",\
  \"step\"       : 3600}]"

