import pymysql

database_config = {
        'host':'localhost',
        'user':'root',
        'password':'Qwer@1234',
        'db':'zabbix',
        'charset':'utf8',
        'table':'host_info'}

def _database_connection():
    try:
        connection = pymysql.connect(
            host = database_config['host'],
            user = database_config['user'],
            password = database_config['password'],
            db = database_config['db'],
            charset = database_config['charset'],
            cursorclass= pymysql.cursors.DictCursor
        )
        print("connection zabbix Database success")
        return connection, connection.cursor()
    except Exception as e:
        print("connection zabbix Database fault")
        print(e)
        return 0

def _database_close(cursor, connection):
    cursor.close()#关闭游标
    connection.close()#关闭连接
    return 0

def database_read(sql):
    connection, cursor = _database_connection()
    cursor.execute(sql)
    result = cursor.fetchall()
    _database_close(connection, cursor)
    return result

def database_execute_commit(sql):
    connection, cursor = _database_connection()
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        connection.rollback()
    _database_close(connection, cursor)
    return

