n=int(input("\nEnter the number of words\n"))
p=input("\nEnter the prefix\n")

cpre=0
for i in range (n):
    w=input("\nEnter a word\n")
    if w.startswith(p)==True:
        cpre+=1
print("\n",cpre,"\n")
