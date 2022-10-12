# 1. 运行服务

### 1.1 flask运行
```
nohup python flask_server.py &
```
### 1.2 gunicorn运行
```
gunicorn -w 4 -b 0.0.0.0:9999 flask_server:app
```

### 1.3 supervisor监控运行
```
/root/miniconda3/envs/flask_server/bin/supervisord -c supervisor.conf

```

# 2. 调用API

ptython,js调用api详细方式请看**flask_api.py**

共提供CRUD，5个API。
```
@app.route('/read/', methods=['GET'])

@app.route('/read_one/', methods=['GET'])

@app.route('/create/', methods=['POST'])

@app.route('/delete/<host_id>/', methods=['POST'])

@app.route('/update/<host_id>/', methods=['POST'])
```

# 3. 管理supervisor
```

supervisord -c supervisor.conf                             通过配置文件启动supervisor
supervisorctl -c supervisor.conf status                    察看supervisor的状态
supervisorctl -c supervisor.conf reload                    重新载入 配置文件
supervisorctl -c supervisor.conf start [all]|[appname]     启动指定/所有 supervisor管理的程序进程
supervisorctl -c supervisor.conf stop [all]|[appname]      关闭指定/所有 supervisor管理的程序进程
-----------------------------------------------------------
supervisorctl

reread读取配置
update更新配置
start/stop all 开启/关闭配置
status 查看状态
```


# 4. mysql 表结构

### 4.1 创建表
```
CREATE TABLE host_info  (
  id int NOT NULL AUTO_INCREMENT,
  host_id varchar(255) NOT NULL,
  host_name varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL COMMENT '名称',
  area varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL COMMENT '区域',
  longitude varchar(255) NULL DEFAULT NULL COMMENT '经度',
  latitude varchar(255) NULL DEFAULT NULL COMMENT '纬度',
  ip varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL COMMENT 'ip地址',
  group_id varchar(255) NULL DEFAULT NULL COMMENT '组',
  host_type varchar(255) NULL,
  PRIMARY KEY (id) USING BTREE
) ENGINE = InnoDB;
```
## 4.2 插入表
```
insert into host_info  (
  host_id,
  host_name,
  area,
  longitude,
  latitude,
  ip,
  group_id,
  host_type)
  values(
    '123456789',
    'first_test_zabbix_host',
    'HuaNan',
    '22.15515',
    '113.521717',
    '192.168.1.6',
    '1',
    'win_server2007');
```