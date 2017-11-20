
import logging

from flask import Flask
from flask import render_template 

main = Flask(__name__)

logging.basicConfig(
        filename='myapp.log', 
        level=logging.INFO, 
        #format='%(asctime)s : [%(filename)s-%(lineno)d] : %(levelname)s : %(message)s', 
        format = '[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
        #datefmt='%m/%d/%Y %I:%M:%S %p'
        )

@main.route('/', methods=['GET'])
def index():
    logging.info('Finished')
    logging.debug('This message should appear on the console')
    logging.warning('And this, too')
    return 'index ok.'


if __name__ == '__main__':


    logging.info('Started')
    main.run(host='0.0.0.0', port=9000, debug=False)
