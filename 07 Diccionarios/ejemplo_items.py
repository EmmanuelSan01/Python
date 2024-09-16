d_categoria={1:25000,2:30000,3:40000,4:45000,5:60000}
print(d_categoria.items())
for k, v in d_categoria.items():
    print(k,v)
d_categoria.pop(4)
print(d_categoria)
for v in d_categoria.values():
    print(v)