import os
import logging
import logging.handlers

from flask import Flask
from flask import current_app


app = Flask(__name__)

# log configure
app.logger.setLevel(logging.INFO)
info_file_handler = logging.handlers.RotatingFileHandler('opsweb.log', maxBytes=1048576, backupCount=20)
info_file_handler.setLevel(logging.INFO)
info_file_handler.setFormatter(
    logging.Formatter('[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s')
)
app.logger.addHandler(info_file_handler)







# email
from logging.handlers import SMTPHandler

ADMINS = ['liqianglau@outlook.com']
# SMTPHandler(self, mailhost, fromaddr, toaddrs, subject, credentials=None, secure=None)
#mail_handler = SMTPHandler('smtp.qq.com', '467754239@qq.com', ADMINS, 'YourApplication Failed', ('467754239@qq.com', 'zys@1326007198'))
mail_handler = SMTPHandler('smtp.163.com', '13260071987@163.com', '467754239@qq.com', 'ceshi demo', ('13260071987@163.com', 'yi15093547036'))
mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(
    logging.Formatter('[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s')
)
app.logger.addHandler(mail_handler)


@app.route('/')
def index():

    current_app.logger.info('current app logger info')
    current_app.logger.error('current app logger info')

    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
