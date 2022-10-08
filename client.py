import requests

kw = {'table_name':'zabbix_demo'}
stat = requests.get("http://localhost:8000/read", params = kw)
print(stat.content)