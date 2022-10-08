from flask import Flask, request, Response
import utils
import json

config = {
    'table_name':'host_info'
}

app = Flask(__name__)

@app.route('/read')
def read_data():
    # 解析requests
    sql = 'select * from {};'.format(config['table_name'])
    # 执行sql
    connection, cursor = utils.connection_database()
    cursor.execute(sql)
    result = cursor.fetchall()
    utils.close_database(connection, cursor)
    return result

@app.route('/create', methods=['POST'])
def create_data():
    parms = json.loads(request.get_data(as_text=True))
    keys = ','.join(list(parms.keys()))
    values = ','.join(["'" + i + "'" for i in list(parms.values())])
    sql = "insert into {} ({}) values ({});".format(config['table_name'], keys, values)
    # 执行sql
    connection, cursor = utils.connection_database()
    try:
        cursor.execute(sql)
        # 提交到数据库执行
        connection.commit()
    except:
        # 如果发生错误则回滚
        connection.rollback()
    # 关闭sql
    utils.close_database(connection, cursor)
    return {'stat':200}

@app.route('/delete/<host_id>/', methods=['POST'])
def delete_data(host_id):
    connection, cursor = utils.connection_database()
    sql = 'delete from {} where host_id = {};'.format(config['table_name'], host_id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        connection.commit()
    except:
        # 发生错误时回滚
        connection.rollback()
    utils.close_database(connection, cursor)
    return {'stat':200}

@app.route('/update/<host_id>/', methods=['POST'])
def update_data(host_id):
    parms = json.loads(request.get_data(as_text=True))
    update_parms = ','.join([i + "='" + parms[i] + "'" for i in parms])
    sql = 'update {} set {} where host_id = {};'.format(config['table_name'], update_parms, host_id)
    connection, cursor = utils.connection_database()
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        connection.commit()
    except:
        # 发生错误时回滚
        connection.rollback()
    utils.close_database(connection, cursor)
    return {'stat':200}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)


