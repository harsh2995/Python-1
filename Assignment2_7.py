x=input("Enter text : ")

for i in x:
    if (i.isdigit()):
        y=0
    else:
        y=1
        break;

if (y==0):
    print("True")
else:
    print("False")
