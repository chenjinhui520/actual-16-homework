#coding: utf-8

import json


def counterLog(filename):
    ret = {}
    with open(filename, 'r') as fd:
        for line in fd:
            token = line.split()
            src_ip = token[0]
            target_url = token[6]
            if src_ip in ret:
                if target_url in ret[src_ip]:
                    ret[src_ip][target_url] += 1
                else:
                    ret[src_ip][target_url] = 1
            else:
                ret[src_ip] = { target_url : 1 }
    return ret

def printJson(data):
    print json.dumps(data, indent=4)


if __name__ == '__main__':
    data = counterLog('logs/access.log')
    printJson(data)
