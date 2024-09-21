import json
import pprint

with open("08 Archivos/datos.json","r") as fd:
    estructura=json.load(fd)
pprint.pprint(estructura)
print(type(estructura))