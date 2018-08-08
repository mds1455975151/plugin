#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import json
import time

# Define the variables used when Falcon reports data
falconTs = int(time.time())
falconTimeStamp = 60
falconPayload = []
falconTag = "DBProxy"


def get_fpnn_data():
    result = os.popen('cd /home/DBProxy &&./cmd 127.0.0.1 12321 *infos {} 1 1').read()
    result = result.replace('Return:', '')
    json_data = json.loads(result)
    return json_data


def get_endpoint():
    f = open("/usr/local/open-falcon/agent/config/cfg.json")
    setting = json.load(f)
    endpoint = setting['hostname']
    return endpoint


def generate_data():
    json_data = get_fpnn_data()
    value = json_data['FPNN.status']['server']['status']['currentConnections']
    temp_dict = {
        "endpoint": get_endpoint(),
        "metric": "FPNN.server.currentConnections",
        "timestamp": falconTs,
        "step": falconTimeStamp,
        "value": value,
        "counterType": "GAUGE",
        "tags": falconTag,
    }
    falconPayload.append(temp_dict)
    fpnn_stat_dict = json_data['FPNN.status']['server']['stat']
    for key, value in fpnn_stat_dict.items():
        for akey, avalue in value.items():
            stat_dict = {
                "endpoint": get_endpoint(),
                "metric": "FPNN.server.stat" + key + "." + akey,
                "timestamp": falconTs,
                "step": falconTimeStamp,
                "value": avalue,
                "counterType": "GAUGE",
                "tags": falconTag,
            }
            falconPayload.append(stat_dict)
    return falconPayload


if __name__ == "__main__":
    falconPayload = generate_data()
    print(json.dumps(falconPayload))
