from operator import truediv
from random import randrange
from math import ceil

portefeuille=int(input("quelle est votre cagnotte: "))
    
#tant que l'on a de l'argent
while portefeuille>=1:
    while True:
        mise=int(input("quelle est votre mise de départ: "))
        if (mise >1) and (mise <= portefeuille ) :
            break
        elif mise > portefeuille :
            print("Vous n'avez pas la somme requise!!")   
        else:
            print("erreur de saisie!")

        
            
         
    x=randrange(50)
    choix=int(input("Choissisez un numéro entre 0 et 49: "))
    
       
    print("le numéro gangant est le ",x)
    
#si gain
    if choix == x :
        portefeuille= portefeuille - mise + (mise * 3)
        print("Félicitations vous avez trouvé le bon nombre, vous avez gagné", mise*3,"€!")
        print("Il vous reste",portefeuille,"euros!" )
#si bonne couleur
    elif choix % 2 == x % 2 :
        portefeuille = portefeuille - ceil(mise/2) 
        print("Félicitation vous avez la bonne couleur", ceil(mise/2), "€")
        print("Il vous reste",portefeuille,"euros!" )
#si on perd
    else: portefeuille = portefeuille - mise 
    print("Vous avez perdu votre mise")
    print("Il vous reste",portefeuille,"euros!" )
if portefeuille<= 0:
    print("Banqueroute!! Au revoir!!!")
        