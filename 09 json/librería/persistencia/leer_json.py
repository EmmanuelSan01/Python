import json
import pprint

with open("09 json\librería\persistencia\datos.json","r") as fd:
    estructura=json.load(fd)
pprint.pprint(estructura)
print(type(estructura))