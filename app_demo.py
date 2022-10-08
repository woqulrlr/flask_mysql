import json

from flask import Flask, request

import utils

config = {
    'table_name':'host_info'
}

app = Flask(__name__)

@app.route('/read')
def read_data():
    sql = 'select * from {};'.format(utils.database_config['table'])
    result = utils.database_read(sql)
    return result

@app.route('/create', methods=['POST'])
def create_data():
    parms = json.loads(request.get_data(as_text=True))
    key_str = ','.join(list(parms.keys()))
    value_str = ','.join(["'" + i + "'" for i in list(parms.values())])
    sql = "insert into {} ({}) values ({});".format(utils.database_config['table'], key_str, value_str)
    utils.database_execute_commit(sql)
    return {'stat':200}

@app.route('/delete/<host_id>/', methods=['POST'])
def delete_data(host_id):
    sql = 'delete from {} where host_id = {};'.format(utils.database_config['table'], host_id)
    utils.database_execute_commit(sql)
    return {'stat':200}

@app.route('/update/<host_id>/', methods=['POST'])
def update_data(host_id):
    parms = json.loads(request.get_data(as_text=True))
    updata_str = ','.join([i + "='" + parms[i] + "'" for i in parms])
    sql = 'update {} set {} where host_id = {};'.format(utils.database_config['table'], updata_str, host_id)
    utils.database_execute_commit(sql)
    return {'stat':200}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)


