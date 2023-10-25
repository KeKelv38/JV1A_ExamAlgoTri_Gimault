#ps: je n'ai pas réussi a fair fonctionner les fonctions, j'ai essayé autrement.

#1
    #def grille(case1,case2,case3,case4,case5,case6,case7,case8,case9):

case1=1
case2=2
case3=3
case4=4
case5=5
case6=6
case7=7
case8=8
case9=9
    
print(case1,"*",case2,"*",case3)
print("* * * * *")
print(case4,"*",case5,"*",case6)
print("* * * * *")
print(case7,"*",case8,"*",case9)

#grilleMorpion=grille
#print(grilleMorpion)

#2
grilleRemplie=False
while ((case1 and case2 and case3 and case4 and case5 and case6 and case7 and case8 and case9)!="X" or "O"):

    caseChoisie=int(input("Joueur 1, veuillez poser votre X dans la case de votre choix\n"))
    if caseChoisie==case1:
        case1="X"
    if caseChoisie==case2:
        case2="X"
    if caseChoisie==case3:
        case3="X"
    if caseChoisie==case4:
        case4="X"
    if caseChoisie==case5:
        case5="X"
    if caseChoisie==case6:
        case6="X"
    if caseChoisie==case7:
        case7="X"
    if caseChoisie==case8:
        case8="X"
    if caseChoisie==case9:
        case9="X"

    print(case1,"*",case2,"*",case3)
    print("* * * * *")
    print(case4,"*",case5,"*",case6)
    print("* * * * *")
    print(case7,"*",case8,"*",case9)

    caseChoisie=int(input("Joueur 2, veuillez poser votre O dans la case de votre choix\n"))
    if caseChoisie==case1:
        case1="O"
    if caseChoisie==case2:
        case2="O"
    if caseChoisie==case3:
        case3="O"
    if caseChoisie==case4:
        case4="O"
    if caseChoisie==case5:
        case5="O"
    if caseChoisie==case6:
        case6="O"
    if caseChoisie==case7:
        case7="O"
    if caseChoisie==case8:
        case8="O"
    if caseChoisie==case9:
        case9="O"

    print(case1,"*",case2,"*",case3)
    print("* * * * *")
    print(case4,"*",case5,"*",case6)
    print("* * * * *")
    print(case7,"*",case8,"*",case9)

print("Partie finie.")

#3 Pas fait
#4 J'ai essayé avec le "while" mais je n'ai pas réussi
#5 Pas fait

#6 -Changer la taille du tableau
#  -Changer les conditions de victoire en vérifiant si le joueur a aligner 4 symboles au lieu de 3
#  -le joueur peut choisir qu'un colonne et non la ligne avec, le symbole part de la plus haute case pour descendre au plus bas possible en fonction des autres symboles.
