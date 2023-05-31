import requests


BASE_URL = 'http://prod-lnx-1:8081/service/rest/v1/blobstores/file'
path_input = "docker_test02"
new_blob_store = {
"softQuota": {
"type": "spaceRemainingQuota",
"limit": 10
},
"path": "docker_test",
"name": "docker_test"
}
response = requests.post(BASE_URL, json=new_blob_store, auth=('admin', 'admin'))
print (response.json)