myTable=[2,5,6,4,1,3]
print(myTable)
stock1=0

case1Choisie=int(input("Saisir une case du tableau\n"))
case2Choisie=int(input("Saisir une autre case du tableau pour intervertir avec le premier choix\n"))

stock1=myTable[case1Choisie]
myTable[case1Choisie]=myTable[case2Choisie]
myTable[case2Choisie]=stock1


print(myTable)



