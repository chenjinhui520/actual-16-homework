#!/usr/bin/env python
#coding:utf-8

import hashlib


def encryption(dstr):
    md5sum = hashlib.md5(dstr)
    return md5sum.hexdigest()



