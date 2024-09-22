import json

#lista=["Daniel","María","Ada","Julián","Gabriel",["Julián","Ricardo"]]
campers={
    1:{
        "nombre":"Daniel",
        "edad":21,
        "sexo":"m",
        "teléfonos":[123,456]
    },
    2:{
        "nombre":"María",
        "edad":20,
        "sexo":"f",
        "teléfono":[789]
    }
}

with open("09 json\librería\persistencia\datos.json","w") as fd:
    json.dump(campers,fd)
if not fd.closed: #True si el archivo está cerrado
    fd.close()