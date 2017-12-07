#!/usr/bin/env python
#coding:utf-8
import logging
from app import app

if __name__ == '__main__':
    LOG_FILE = '/tmp/myapp.log'
    logging.basicConfig(
            filename=LOG_FILE,
            level=logging.INFO,
            format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s'
            )
    logging.debug('started')
    app.run(host='0.0.0.0', port=9000, debug=True)

