import json
import logging
import logging.handlers

from flask import Flask, request
from flask_cors import CORS

import utils
import flask_server_log

app = Flask(__name__)
CORS(app, supports_credentials=True)

flask_server_log.log_config()

@app.route('/read')
def read_data():
    try:
        sql = 'select * from {};'.format(utils.database_config['table'])
        result = utils.database_read(sql)
        return result
    except Exception as e:
        logging.exception(e)
        logging.warning(request.url)
        logging.warning(request.data)

@app.route('/create', methods=['POST'])
def create_data():
    try:
        parms = json.loads(request.get_data(as_text=True))
        key_str = ','.join(list(parms.keys()))
        value_str = ','.join(["'" + i + "'" for i in list(parms.values())])
        sql = "insert into {} ({}) values ({});".format(utils.database_config['table'], key_str, value_str)
        utils.database_execute_commit(sql)
        return {'stat':200}
    except Exception as e:
        logging.exception(e)
        logging.warning(request.url)
        logging.warning(request.data)

@app.route('/delete/<host_id>/', methods=['POST'])
def delete_data(host_id):
    try:
        sql = 'delete from {} where host_id = {};'.format(utils.database_config['table'], host_id)
        utils.database_execute_commit(sql)
        return {'stat':200}
    except Exception as e:
        logging.exception(e)
        logging.warning(request.url)
        logging.warning(request.data)

@app.route('/update/<host_id>/', methods=['POST'])
def update_data(host_id):
    try:
        parms = json.loads(request.get_data(as_text=True))
        updata_str = ','.join([i + "='" + parms[i] + "'" for i in parms])
        sql = 'update {} set {} where host_id = {};'.format(utils.database_config['table'], updata_str, host_id)
        utils.database_execute_commit(sql)
        return {'stat':200}
    except Exception as e:
        logging.exception(e)
        logging.warning(request.url)
        logging.warning(request.data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)


