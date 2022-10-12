import requests

# Read API JavaScript - Fetch: url/read/
'''
var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

fetch("http://127.0.0.1:9999/read", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
'''

url = "http://127.0.0.1:9999/read"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# Read API JavaScript - Fetch: url/read_one/
# params: 444444444?group_id=3&ip=192.168.1.212&host_name=2222_test_zabbix_host
'''
var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

fetch("http://127.0.0.1:9999/read_one/?ip=192.168.1.212", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
'''

import requests

url = "http://127.0.0.1:9999/read_one/?ip=192.168.1.212"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)




# Create API JavaScript - Fetch: url/create/
'''
var myHeaders = new Headers();
myHeaders.append("Content-Type", "text/plain");

var raw = "{\r\n    \"host_id\":\"222222222\",\r\n    \"host_name\":\"2222_test_zabbix_host\",\r\n    \"area\":\"Macao\",\r\n    \"longitude\":\"22.15515\",\r\n    \"latitude\":\"113.521717\",\r\n    \"ip\":\"192.168.1.212\",\r\n    \"group_id\":\"3\",\r\n    \"host_type\":\"Linux\"\r\n}";

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("http://127.0.0.1:9999/create", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
'''

url = "http://127.0.0.1:9999/create"

payload = "{\r\n    \"host_id\":\"222222222\",\r\n    \"host_name\":\"2222_test_zabbix_host\",\r\n    \"area\":\"Macao\",\r\n    \"longitude\":\"22.15515\",\r\n    \"latitude\":\"113.521717\",\r\n    \"ip\":\"192.168.1.212\",\r\n    \"group_id\":\"3\",\r\n    \"host_type\":\"Linux\"\r\n}"
headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


# Delete API JavaScript - Fetch: url/delete/<host_id>/
'''
var raw = "";

var requestOptions = {
  method: 'POST',
  body: raw,
  redirect: 'follow'
};

fetch("http://127.0.0.1:9999/delete/222222222", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
'''

url = "http://127.0.0.1:9999/delete/222222222"

payload = ""
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


# Update API JavaScript - Fetch: url/update/<host_id>/
'''
var myHeaders = new Headers();
myHeaders.append("Content-Type", "text/plain");

var raw = "{\r\n    \"area\":\"Macao_must\"\r\n}";

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("http://127.0.0.1:9999/update/222222222", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
'''

url = "http://127.0.0.1:9999/update/222222222"

payload = "{\r\n    \"area\":\"Macao_must\"\r\n}"
headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
