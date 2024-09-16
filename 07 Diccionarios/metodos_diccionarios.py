#DICCIONARIOS

#crear un diccionario vacío
dCampers={}
dCampers=dict()
print(dCampers)

dCampers={1:"Ada",2:"Juan",3:"Diego",4:"Oscar",5:"Anderson"}
print(dCampers)
print(dCampers.setdefault(4)) #existe la llave
dCampers.setdefault(6,"María")
print(dCampers)