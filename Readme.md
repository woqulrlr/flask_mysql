#创建表
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

#插入表
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