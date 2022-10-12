import json
import logging
import logging.handlers

from flask import Flask, request, jsonify
from flask_cors import CORS

import utils
import flask_log

app = Flask(__name__)
CORS(app, supports_credentials=True)

flask_log.log_config()

@app.route('/read/')
def read_data():
    try:
        sql = 'select * from {};'.format(utils.database_config['table'])
        result = utils.database_read(sql)
        return jsonify({'data':result,'statue_code':200})
    except Exception as e:
        logging.exception(e)
        logging.warning(request.url)
        logging.warning(request.data)
        return jsonify({'data':[],'statue_code':400})

@app.route('/read_one/')
def read_one_data():
    try:
        params_dict = request.args.to_dict()
        params_list = ['{} = {!r}'.format(i, params_dict[i]) for i in params_dict]
        params_str = ' and '.join(params_list)
        sql = 'select * from {} where {};'.format(utils.database_config['table'], params_str)
        result = utils.database_read(sql)
        return jsonify({'data':result,'statue_code':200})
    except Exception as e:
        logging.exception(e)
        logging.warning(request.url)
        logging.warning(request.data)
        return jsonify({'data':[],'statue_code':400})

@app.route('/create/', methods=['POST'])
def create_data():
    try:
        params = json.loads(request.get_data(as_text=True))
        key_str = ','.join(list(params.keys()))
        value_str = ','.join(["'" + i + "'" for i in list(params.values())])
        sql = "insert into {} ({}) values ({});".format(utils.database_config['table'], key_str, value_str)
        utils.database_execute_commit(sql)
        return jsonify({'data':[],'statue_code':200})
    except Exception as e:
        logging.exception(e)
        logging.warning(request.url)
        logging.warning(request.data)
        return jsonify({'data':[],'statue_code':400})

@app.route('/delete/<host_id>/', methods=['POST'])
def delete_data(host_id):
    try:
        sql = 'delete from {} where host_id = {};'.format(utils.database_config['table'], host_id)
        utils.database_execute_commit(sql)
        return jsonify({'data':[],'statue_code':200})
    except Exception as e:
        logging.exception(e)
        logging.warning(request.url)
        logging.warning(request.data)
        return jsonify({'data':[],'statue_code':400})

@app.route('/update/<host_id>/', methods=['POST'])
def update_data(host_id):
    try:
        params = json.loads(request.get_data(as_text=True))
        updata_str = ','.join([i + "='" + params[i] + "'" for i in params])
        sql = 'update {} set {} where host_id = {};'.format(utils.database_config['table'], updata_str, host_id)
        utils.database_execute_commit(sql)
        return jsonify({'data':[],'statue_code':200})
    except Exception as e:
        logging.exception(e)
        logging.warning(request.url)
        logging.warning(request.data)
        return jsonify({'data':[],'statue_code':400})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)