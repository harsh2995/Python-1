slist=[]
x=input("Enter a string with special characters : ")

for i in x:
    if(ord(i)>32 and ord(i)<48):
        slist.append(i)

print(slist)
