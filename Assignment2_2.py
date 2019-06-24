numlist=[]
for i in range(1,22):
    for j in range(i+1,21):
        if ((i+j)%2==0 and (i+j) in range(21)):
            numlist.append(tuple((i,j)))

print(numlist)
