# Compléter ici (noms, groupe, contenu fichier, date)
# Mamadou Radjaye sow , le 21/11/2025 Traite de Jeu du Tic Tac Toe
#
#
#
# Ne pas supprimer cette ligne. <trace>tictactoe.py</trace>


####################
# Jeu du Tic Tac Toe
####################
import random
from copy import deepcopy


#Affichage

def affiche_motif():
    """ Affiche le motif
    Précondition :
    Exemple(s) :
    $$$ 
    """
    print('+---+---+---+')
def affiche_barre(i:int,j:int,k:int):
    """ Affiche les barres
    
    Précondition : 
    Exemple(s) :
    $$$ 
    """
    print(f'| {i} | {j} | {k} |')
    
    
def affichage_grille(grille:list[list[str]]) -> None:
    """ Affiche la grille

    Précondition :
    """
    for i in range(3):
        affiche_motif()
        affiche_barre(grille[i][0],grille[i][1],grille[i][2])
    affiche_motif()

# Saisie


def saisie_nom()->str:
    """ Saisie le nom
    Précondition : 
    Exemple(s) :
    $$$ 
    """
    nom=input("Saisir votre nom: ")
    while nom=='':
        nom=input("Saisir votre nom: ")
    return nom
    
    

def saisie_nom_different(nom)->str:
    """ Saisie le deuxieme non
    Précondition : 
    Exemple(s) :
    $$$ 
    """
    nom2=input("Saisir le second nom: ")
    while nom2=='' or nom2==nom :
        nom2=input("Saisir le second nom: ")
    return nom2
def saisie_coordonne()->list[int]:
    """ Saisie les coordonne de la case ( ligne et colonne)

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    indice_ligne=int(input(" Entrer l'indice de la ligne: "))
    while indice_ligne>=3:
         indice_ligne=int(input(" Entrer l'indice de la ligne(0 a 2): "))
         
    indice_col=int(input(" Entrer l'indice de la colonne: "))
    while indice_col>=3:
        indice_col=int(input(" Entrer l'indice de la colonne(0 a 2): "))
        
    return [indice_ligne,indice_col]
    
    
    

# Analye et Traitement


def tous_sont_identique(liste:list[str])->bool:
    """ Renvoie True si tous les elements sont non vides, identiques et len(liste)==3 

    Précondition : 
    Exemple(s) :
    $$$ tous_sont_identique(['a','a','a'])
    True
    $$$ tous_sont_identique(['a','','a'])
    False
    $$$ tous_sont_identique(['b','b','a'])
    False
    $$$ tous_sont_identique(['b','a'])
    False
    $$$ tous_sont_identique(['','a','a'])
    False
    """
    if len(liste)<3 :
        return False
    
    
    prec=liste[0]

    for elt in liste[1:]:
        if prec =='' or prec!=elt:
            return False
    return True 
            
            
        
def est_vide(grille:list[list[str]],i:int,j:int)->bool:
    """ Renvoie True si la case vide

    Précondition : 
    Exemple(s) :
    $$$ est_vide([['X','O',''],['X','','O'],['X','O','O']],0,2)
    True
    $$$ est_vide([['X','O',''],['X','','O'],['X','O','O']],1,1)
    True
    $$$ est_vide([['X','O',''],['X','','O'],['X','O','O']],2,1)
    False
    """
    return (i<3 and j<3) and grille[i][j]==''
    
def est_aligne_hori(grille:list[list[str]])->bool:
    """ Renvoie True si les case aligne horizontalement sont identiques

    Précondition : 
    Exemple(s) :
    $$$ est_aligne_hori([['X','X','X'],['X','','O'],['X','O','O']])
    True
    $$$ est_aligne_hori([['X','O',''],['O','O','O'],['X','O','O']])
    True
    $$$ est_aligne_hori([['X','O',''],['X','','O'],['X','O','O']])
    False
    $$$ est_aligne_hori([['','',''],['','',''],['','','']])
    False
    """
    for ligne in grille:
        if tous_sont_identique(ligne):
            return True
    return False 
           
def est_aligne_verti(grille:list[list[str]])->bool:
    """  Renvoie True si les case aligne verticalement sont identiques 

    Précondition : 
    Exemple(s) :
    $$$ est_aligne_verti([['X','X','X'],['X','','O'],['X','O','O']])
    True
    $$$ est_aligne_verti([['','O',''],['X','O','O'],['X','O','O']])
    True
    $$$ est_aligne_verti([['O','',''],['X','','O'],['X','','O']])
    False
    $$$ est_aligne_verti([['X','O','X'],['X','','O'],['O','','O']])
    False
    $$$ est_aligne_verti([['','',''],['','',''],['','','']])
    False
    $$$ est_aligne_verti([['','',''],['','X',''],['','','']])
    False
    """
    liste_temp=[]
    for i in range(3):
        for j in range(3):
            liste_temp.append(grille[j][i])
        if tous_sont_identique(liste_temp):
            return True
        else:
            liste_temp=[]
    return False


    
def est_aligne_diago(grille:list[list[str]])->bool:
     """ Renvoie True si les case aligne diagonalement sont identiques

     Précondition : 
     Exemple(s) :
     $$$ est_aligne_diago([['X','X','X'],['X','X','O'],['X','O','X']])
     True
     $$$ est_aligne_diago([['','O','O'],['X','O','O'],['O','','O']])
     True
     $$$ est_aligne_diago([['O','',''],['X','','O'],['','','O']])
     False
     $$$ est_aligne_diago([['X','O','X'],['X','','O'],['O','','O']])
     False 
     $$$ est_aligne_diago([['','',''],['','',''],['','','']])
     False
     $$$ est_aligne_diago([['','',''],['','X',''],['','','']])
     False
     """
     liste_temp0=[]
     liste_temp1=[]
     for i in range(3):
         liste_temp0.append(grille[i][i])
         liste_temp1.append(grille[2-i][i])
     grille_temp=[liste_temp0,liste_temp1]
     for liste in grille_temp:
         if  tous_sont_identique(liste):
             return True
     return False
    
def mise_Ajour(grille:list[list[str]],i:int,j:int,choix:str)->list[list[str]]:
    """ Renvoie une grille mise a jour

    Précondition : 
    Exemple(s) :
    $$$ g= mise_Ajour([['','O','O'],['X','O','O'],['O','','O']],0,0,'X')
    $$$ g
    [['X','O','O'],['X','O','O'],['O','','O']]
    $$$ g= mise_Ajour([['','O','O'],['X','O','O'],['X','','O']],2,1,'O')
    $$$ g
    [['','O','O'],['X','O','O'],['X','O','O']]
    """
    nouv_grille=deepcopy(grille)
    nouv_grille[i][j]=choix
    return nouv_grille

def trouver(grille:list[list[str]])->bool:
    """ Renvoie True si au moins un alignement est vrai

    Précondition : 
    Exemple(s) :
    $$$ trouver([['X','X','X'],['X','X','O'],['X','O','X']])
    True
    $$$ trouver([['O','',''],['X','','O'],['X','','O']])
    False
    $$$ trouver([['','',''],['','',''],['','','']])
    False
    $$$ trouver([['','',''],['','X',''],['','','']])
    False
    """
    return est_aligne_diago(grille) or  est_aligne_hori(grille) or  est_aligne_verti(grille)
    
    
    
def grille_vide() -> list[list[str]]:
    """ Renvoie une grille initialise

    Précondition :
    Exemple(s) :
    $$$ 
    """
    grille = []
    ligne = ["","",""]
    for i in range(3):
        grille.append(ligne.copy())
    return grille

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
                   
       
def jouer() -> None:
    grille=grille_vide()
    joueur1=saisie_nom()
    joueur2=saisie_nom_different(joueur1)
    ljoueur=[joueur1,joueur2]
    choix=['X','O']
    indice_alea=random.randint(0,1)
    indice_joueur_courant=indice_alea
    gagnant=''
    message=''
    i=0
    affichage_grille(grille)
    while i<=8 and not trouver(grille):
        joueur=ljoueur[indice_joueur_courant]
        print(f"{joueur} : à vous !")
        liste_coor=saisie_coordonne()
        while not est_vide(grille,liste_coor[0],liste_coor[1]):
            print('Cette case est occupee')
            liste_coor=saisie_coordonne()
        grille=mise_Ajour(grille,liste_coor[0],liste_coor[1],choix[indice_joueur_courant])
        i+=1
        if trouver(grille) :
            gagnant=joueur
            message=f'Bravo ! {gagnant} a gagne'
        elif i==8:
             message='Match nul !'
             
        else:
            indice_joueur_courant=indice_autre_joueur(indice_joueur_courant)
        affichage_grille(grille) 
    return print(message)
 
if __name__ == '__main__':
    jouer()
   