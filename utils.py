import pymysql

def connection_database():
    try:
        connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'Qwer@1234',
            db = 'zabbix',
            charset = 'utf8',
            cursorclass= pymysql.cursors.DictCursor
        )
        print("connection zabbix Database success")
        return connection, connection.cursor()
    except Exception as e:
        print("connection zabbix Database fault")
        print(e)
        return 0

def close_database(cursor, connection):
    cursor.close()#关闭游标
    connection.close()#关闭连接
    return 0

def 