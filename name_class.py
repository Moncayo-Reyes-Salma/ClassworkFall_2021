import requests

server_name = "http://vcm-21170.vm.duke.edu:5000/"

r = requests.get(server_name + "student")
request_json = {
   "name": "Salma Moncayo-Reyes",
   "net_id": "sjm99",
   "e-mail": "salma.moncayoreyes@duke.edu"
}

s = requests.post(server_name + "student", json=request_json)
