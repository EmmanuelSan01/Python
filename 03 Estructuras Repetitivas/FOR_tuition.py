tuition=10000
for i in range(1,100):
    increase=tuition*0.07
    tuition+=increase
    if tuition>=20000:
        break
print("The tuition will have doubled in",i,"years")