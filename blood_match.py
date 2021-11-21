import requests

server_name = "http://vcm-7631.vm.duke.edu:5002/"

r = requests.get(server_name + "get_patients/sjm99")
print(r.text)

s = requests.get(server_name + "get_blood_type/M2")
print(s.text)

t = requests.get(server_name + "get_blood_type/F4")
print(t.text)


request_json = {"Name": "sjm99", "Match": "Yes"}
q = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=request_json)
print(q.text)
