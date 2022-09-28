import requests
import configparser

l1={ "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }
l2={ "payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z" }
l3={ "payer": "DANNON", "points": -200, "timestamp": "2020-10-31T15:00:00Z" }
l4={ "payer": "MILLER COORS", "points": 10000, "timestamp": "2020-11-01T14:00:00Z" }
l5={ "payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z" }
config = configparser.ConfigParser()
config.read("configfile.ini")
url_add = config["API"]["addtrans"]
url_spend=config["API"]["spend"]
url_total=config["API"]["balance"]

session = requests.Session()
r = session.post(url_add, json=l1)
o = session.post(url_add, json=l2)
p = session.post(url_add, json=l3)
e = session.post(url_add, json=l4)
m = session.post(url_add, json=l5)
ge=session.post(url_spend, json={"points": 5000})
response=session.get(url_total)
print(r.text)
print(o.text)
print(p.text)
print(e.text)
print(m.text)
print(ge.text)
print(response.text)