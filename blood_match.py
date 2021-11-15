import requests

server_name = "http://vcm-7631.vm.duke.edu:5002/"

r = requests.get(server_name + "get_patients/sjm99")
print(r.text)

s = requests.get(server_name + "get_blood_type/M2")
print(s.text)

t = requests.get(server_name + "get_blood_type/F4")
print(t.text)

t = requests.post(server_name + "match_check/F4")
request_json = {
   "name": "Salma Moncayo-Reyes",
   "net_id": "sjm99",
   "e-mail": "salma.moncayoreyes@duke.edu"
}
print(t.text)
