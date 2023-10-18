myTable=[6,5,2,4,1,3]
print(myTable)
stock=0
for i in range (len(myTable)):

    if myTable[i]>myTable[i+1]:
        stock=myTable[i]
        myTable[i]=myTable[i+1]
        myTable[i+1]=stock


print(myTable)

#si le chiffre est plus grand que le chiffre d'après
#alors les deux chiffres s'inversent 