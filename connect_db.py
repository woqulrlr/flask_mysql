import sys
import pymysql

# print(sys.executable)
try:
    connection = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'Qwer@1234',
        db = 'zabbix',
        charset = 'utf8',
        cursorclass= pymysql.cursors.DictCursor
    )
    print(connection)
except Exception as e:
    print(e)

sql = 'select * from zabbix_demo;'
cursor = connection.cursor()#获取游标对象
cursor.execute(sql)#执行sql预计
result = cursor.fetchall()
print(result)
cursor.close()#关闭游标
connection.close()#关闭连接