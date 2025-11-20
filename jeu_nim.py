# Compléter ici (noms, groupe, contenu fichier, date)
# Mamadou Radjaye sow MI23 Traite de jeu_nim.py Le 22/10/2025
# 
#
#
# Ne pas supprimer cette ligne. <trace>jeu_nim.py</trace>


####################
# Jeu de Nim
####################

def saisie_nom()->str:
    """
    Précondition : 
    Exemple(s) :
    $$$ 
    """
    nom=input("Saisir votre nom: ")
    while nom=='':
        nom=input("Saisir votre nom: ")
    return nom
    
    

def saisie_nom_different(nom)->str:
    """ 
    Précondition : 
    Exemple(s) :
    $$$ 
    """
    nom2=input("Saisir le second nom: ")
    while nom2=='' or nom2==nom :
        nom2=input("Saisir le second nom: ")
    return nom2
       

    
    

def max_possible_a_prendre(nb_allumettes_courant:int)->int:
    """Renvoie le nombre max d’allumettes à prendre
    Précondition : 
    Exemple(s) :
    $$$ max_possible_a_prendre(34)
    3
    $$$ max_possible_a_prendre(0)
    0
    $$$ max_possible_a_prendre(3)
    3
    """
    maxi=0
    if nb_allumettes_courant>=3:
        maxi=3
    elif nb_allumettes_courant==2:
        maxi=2
    elif nb_allumettes_courant==1:
        maxi=1
   
    return maxi 
    
def reste(pris:int, totale:int)->int:
    """ Renvoies la difference

    Précondition : 
    Exemple(s) :
    $$$ reste(2,34)
    32
    """
    return totale-pris

def saisir_nb_allumettes_prises(max_prise)->int:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    nb_allumettes_prises=int(input("Saisir le nombre d'allumettes a prendre: "))
    while nb_allumettes_prises >max_prise:
        nb_allumettes_prises=int(input(f"Saisir le nombre d'allumettes a prendre inferieur ou egale a {max_prise} : "))
    return nb_allumettes_prises
        

def indice_autre_joueur(indice:int)->int:
    """ 
    Renvoie l'indice de l'autre joueur
    Précondition : 
    Exemple(s) :
    $$$ indice_autre_joueur(1)
    0
    $$$ indice_autre_joueur(0)
    1
    """
    return 1-indice

import random 
def jouer():
    """ 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    nb_allumette_totale=random.randint(10,30)
    joueur1=saisie_nom() 
    joueur2=saisie_nom_different(joueur1)
    ljoueur=[joueur1,joueur2]
    indice_alea=random.randint(0,1)
    indice=indice_alea
    
    gagnant=''

  
    while nb_allumette_totale !=0:
        joueur=ljoueur[indice]
        print(f"Nombre d'allumettes est: {nb_allumette_totale}")
        print(f"{joueur} : à vous !")
        max_prise=max_possible_a_prendre(nb_allumette_totale)
        
        nb_pris=saisir_nb_allumettes_prises(max_prise)
        nb_allumette_totale= reste(nb_pris,nb_allumette_totale)
        if nb_allumette_totale==0:
            gagnant=joueur
        indice=indice_autre_joueur(indice)
        
            
    return print(f"Plus d'allumettes! {gagnant} a gagne")


if __name__ == '__main__':
    jouer()
   
