#!/usr/bin/env python
# coding: utf-8

import logging


logging.basicConfig(
        filename = './logs',
        filemode = 'a',
        format = '[%(asctime)s] - [%(threadName)5s] -[%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
        level = logging.DEBUG,
        datefmt='%m/%d/%y  %I:%M:%S %p'
)


