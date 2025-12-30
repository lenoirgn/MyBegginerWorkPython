# Compléter ici (noms, groupe, contenu fichier, date)
# Mamadou Radjaye sow MI23, Le traite de 2048, le 18/12/2025
#
#
#
# Ne pas supprimer cette ligne. <trace>binairo.py</trace>

from copy import deepcopy
from random import randint
#Affichage

def affiche_motif():
    """ Affiche le motif
    Précondition :
    Exemple(s) :
    $$$ 
    """
    print('+---+---+---+---+')
def affiche_barre(i:str,j:str,k:str,l:str):
    """ Affiche les barres
    
    Précondition : 
    Exemple(s) :
    $$$ 
    """
    print(f'| {i} | {j} | {k} | {l} |')
    
    
def affichage_grille(grille:list[list[str]]) -> None:
    """ Affiche la grille

    Précondition :
    """
    for i in range(4):
        affiche_motif()
        affiche_barre(grille[i][0],grille[i][1],grille[i][2],grille[i][3])
    affiche_motif()
    
def menu():
    print("=== MENU DE DÉPLACEMENT ===")
    print("L = Gauche")
    print("R = Droite")
    print("U = Haut")
    print("D = Bas")
    print("============================")
# Traitement et Analyse
def est_vide(grille:list[list[str]],i:int,j:int)->bool:
    """ Renvoie True si la case vide

    Précondition : 
    Exemple(s) :
    $$$ est_vide([['X','O',0],['X','','O'],['X','O','O']],0,2)
    True
    $$$ est_vide([['X','O',''],['X',0,'O'],['X','O','O']],1,1)
    True
    $$$ est_vide([['X','O',''],['X','','O'],['X','O','O']],2,1)
    False
    """
    return (i<4 and j<4) and grille[i][j]==0
def sommer(grille:list[list[int]],i0:int,j0:int,i1:int,j1:int)->list[list[int]]:
    """ Fais la somme de deux cases

    Précondition : 
    Exemple(s) :
    $$$ sommer([[2, 4, 2, 0], [0, 0, 2, 8], [0, 2, 8, 2], [0, 0, 0, 0]],0,0,1,0)
    [[0, 4, 2, 0], [2, 0, 2, 8], [0, 2, 8, 2], [0, 0, 0, 0]]
    $$$ sommer([[2, 4, 2, 0], [0, 0, 2, 8], [0, 2, 8, 2], [0, 0, 0, 0]],2,1,3,1)
    [[2, 4, 2, 0], [0, 0, 2, 8], [0, 0, 8, 2], [0, 2, 0, 0]] 
    """
    new=deepcopy(grille)
    new[i1][j1]+=new[i0][j0]
    new[i0][j0]=0
    return new
def est_identique(grille:list[list[int]],i0:int,j0:int,i1:int,j1:int)->bool:
     """ 

     Précondition : 
     Exemple(s) :
     $$$ est_identique([[2, 4, 2, 0], [2, 0, 2, 8], [0, 2, 8, 2], [0, 0, 0, 0]],0,0,1,0)
     True
     $$$ est_identique([[2, 4, 2, 0], [0, 0, 2, 8], [0, 2, 8, 2], [1, 0, 0, 0]],2,1,3,1)
     False  
     """
     return grille[i1][j1]==grille[i0][j0]
def suivant_meme(liste:list[int])->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ suivant_meme([2, 4, 2, 0])
    False
    $$$ suivant_meme([2, 4, 8, 8])
    True
    $$$ suivant_meme([2, 4, 4, 0])
    True
    $$$ suivant_meme([2, 0, 0, 4])
    False
    """
    prec=liste[0]
    for elet in liste[1:]:
        if prec!=0 and prec==elet:
            return True
        else:
            prec=elet
    return False
        
def indice_meme(liste:list[int])->list[int]:
    """ Renvoie la liste des indices de element identiques successives

    Précondition : 
    Exemple(s) :
    $$$ indice_meme([2, 4, 2, 0])
    []
    $$$ indice_meme([0, 2, 2, 0])
    [1,2]
    $$$ indice_meme([2, 4, 8, 8])
    [2,3]
    """
    
    prec=liste[0]
    i=0
    for elet in liste[1:]:
        if prec!=0 and prec==elet:
            return [i,i+1]
        else:
            prec=elet
            i+=1
    return []
def zero_devant(liste:list[int])->bool:
     """ Renvoi true si le suivant est zero

     Précondition : 
     Exemple(s) :
     $$$ zero_devant([2, 4, 2, 0])
     True
     $$$ zero_devant([2, 4, 8, 8])
     False
     $$$ zero_devant([2, 0, 4, 5])
     True
     $$$ zero_devant([2, 0, 0, 4])
     True
     $$$ zero_devant([0, 0, 0, 0])
     False
     $$$ zero_devant([0, 0, 0, 4])
     False
     """
     prec=liste[0]
     for elet in liste[1:]:
        if prec!=0 and elet==0:
            return True
        else:
            prec=elet
     return False
def indice_zero(liste:list[int])->list[int]:
    """ Renvoie la liste de 0 et son precedent
    Précondition : 
    Exemple(s) :
    $$$ indice_zero([2, 4, 2, 0])
    [2,3]
    $$$ indice_zero([2, 4, 8, 8])
    []
    $$$ indice_zero([2, 0, 4, 5])
    [0,1]
    $$$ indice_zero([2, 0, 0, 4])
    [0,1]
    $$$ indice_zero([0, 0, 0, 0])
    []
    $$$ indice_zero([0, 0, 0, 4])
    [] 
    """
    prec=liste[0]
    i=0
    for elet in liste[1:]:
        if prec!=0 and elet==0:
            return [i,i+1]
        else:
            prec=elet
            i+=1
    return []
    
    
def deplacer(grille:list[list[int]],i:int)->list[list[int]]:
    """
    Précondition : 
    Exemple(s) :
    $$$ deplacer([[2, 4, 2, 0], [0, 0, 2, 8], [0, 2, 8, 2], [0, 0, 0, 0]],0)
    [[0, 2, 4, 2], [0, 0, 2, 8], [0, 2, 8, 2], [0, 0, 0, 0]]
    $$$ deplacer([[2, 2, 2, 0], [0, 0, 2, 8], [2, 2, 8, 2], [0, 0, 0, 0]],0)
    [[0, 0, 4, 2], [0, 0, 2, 8], [2, 2, 8, 2], [0, 0, 0, 0]]
    $$$ deplacer([[2, 2, 2, 0], [0, 0, 2, 8], [2, 2, 4, 8], [0, 0, 0, 0]],2)
    [[2, 2, 2, 0], [0, 0, 2, 8], [0, 0, 0, 16], [0, 0, 0, 0]]
    $$$ deplacer([[0, 2, 2, 2], [8, 2, 0, 0], [8, 4, 2, 2], [0, 0, 0, 0]],2)
    [[0, 2, 2, 2], [8, 2, 0, 0], [0, 0, 0, 16], [0, 0, 0, 0]]
    """
    nouv_grille=deepcopy(grille)
    while suivant_meme(nouv_grille[i]) or zero_devant(nouv_grille[i]) :
       if suivant_meme(nouv_grille[i]):
           indice=indice_meme(nouv_grille[i])
           nouv_grille=sommer(nouv_grille,i,indice[0],i,indice[1])
       if zero_devant(nouv_grille[i]):
           indice0=indice_zero(nouv_grille[i])
           nouv_grille=sommer(nouv_grille,i,indice0[0],i,indice0[1])   
    return nouv_grille

          
def deplacer_droite(grille:list[list[int]])->list[list[int]]:
    """ Deplace le contenu de toute les cases vers la droite

    Précondition : 
    Exemple(s) :
     $$$ deplacer_droite([[2, 2, 2, 0], [0, 0, 2, 8], [2, 2, 4, 8], [0, 0, 0, 0]])
     [[0, 0, 4, 2], [0, 0, 2, 8], [0, 0, 0, 16], [0, 0, 0, 0]]
    """
    nouv_grille=deepcopy(grille)
    for i in range(4):
       nouv_grille= deplacer(nouv_grille,i)
    return nouv_grille
        
 #Gauche
def inverser_liste(liste:list[int])->list[int]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ inverser_liste([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    return liste[::-1]
def inverser_ligne(grille:list[list[int]])->list[list[int]]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ inverser_ligne([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]
    """
    nouv_grille=deepcopy(grille)
    for i in range(4):
        nouv_grille[i]=inverser_liste(nouv_grille[i])
    return nouv_grille
        
        
def deplacer_gauche(grille:list[list[int]])->list[list[int]]:
    """ Deplace le contenu de toute les cases vers la gauche

    Précondition : 
    Exemple(s) :
    $$$ deplacer_gauche([[2, 2, 2, 0], [0, 0, 2, 8], [2, 2, 4, 8], [0, 0, 0, 0]])
    [[2, 4, 0, 0], [2, 8, 0, 0], [16, 0, 0, 0], [0, 0, 0, 0]]
    
    """
    nouv_grille=inverser_ligne(grille)
    nouv_grille=deplacer_droite(nouv_grille)
    return inverser_ligne(nouv_grille)
    
    
        
    
 #Bas
def colonne(grille:list[list[int]],ind:int)->list[str]:
    """ Renvoie  la colonne d’indice ind

    Précondition : ind<len(ligne)
    Exemple(s) :
    $$$ colonne([[0,0,3],[0,0,3],[0,0,3]],2)
    [3,3,3]
    """
    colonne=[]
    for i in range(len(grille)):
        colonne.append(grille[i][ind])
    return colonne
    
def transpose(grille:list[list[int]])->list[list[int]]:
    """ Renvoie une nouvelle grille qui est la transposée du paramètre

    Précondition : 
    Exemple(s) :
    $$$ transpose([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
    """
    nouv_grille=[]
    for i in range(len(grille[0])):
        nouv_grille.append(colonne(grille,i))
    return nouv_grille
            
def deplacer_bas(grille:list[list[int]])->list[list[int]]:
    """ Deplace le contenu de toute les cases vers le bas
    Précondition : 
    Exemple(s) :
    $$$ deplacer_bas([[2, 2, 2, 0], [0, 0, 2, 8], [2, 2, 4, 8], [0, 0, 0, 0]])
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [4, 4, 8, 16]]
    """
    nouv_grille=deepcopy(grille)
    nouv_grille= transpose(nouv_grille)
    nouv_grille=deplacer_droite(nouv_grille)
    return transpose(nouv_grille)
def deplacer_haut(grille:list[list[int]])->list[list[int]]:
    """ Deplace le contenu de toute les cases vers le haut
    Précondition : 
    Exemple(s) :
    $$$ deplacer_haut([[2, 2, 2, 0], [0, 0, 2, 8], [2, 2, 4, 8], [0, 0, 0, 0]])
    [ [4, 4, 8, 16],[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """
    nouv_grille=deepcopy(grille)
    nouv_grille=deplacer_bas(nouv_grille)
    return nouv_grille[::-1]
    
    
def  genere(grille:list[list[int]])->list[list[int]]:
    """ Genere alearetoirement du contenu soit 2 ou 4

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    nouv_grille=deepcopy(grille)
    valeur= 2*randint(1,2)
    i=randint(0,3)
    j=randint(0,3)
    while not est_vide(grille,i,j):
        i=randint(0,3)
        j=randint(0,3)
    nouv_grille[i][j]=valeur
    return nouv_grille
    
def grille_vide() -> list[list[int]]:
    """ Renvoie une grille initialise

    Précondition :
    Exemple(s) :
    $$$ 
    """
    grille = []
    ligne = [0,0,0,0]
    for i in range(4):
        grille.append(ligne.copy())
    return grille
def arret(grille:list[list[int]]):
    """ Renvoie True si grille est plein ou 2048 est atteint

    Précondition : 
    Exemple(s) :
    $$$ arret([[2, 2, 2, 0], [0, 0, 2, 8], [2, 2, 4, 8], [0, 0, 0, 0]])
    False
    $$$ arret([[2, 2, 2, 4], [9, 4, 2, 8], [2, 2, 4, 8], [4, 2, 4, 8]])
    True
    $$$ arret([[2, 2, 2, 2048], [9, 4, 2, 8], [2, 2, 4, 8], [4, 2, 4, 8]])
    False
    """
    for ligne in grille:
        if 0 in ligne or  2048 in ligne :
            return False
    return True

def jouer():
    grille=grille_vide()
    alea= randint(1,2)
    affichage_grille(grille)
    menu()
    avis=input("Etes-vous pret a jouer: Y/N ")
    if avis=='Y':
        nouv_grille=genere(grille)
        for i in range(alea):
            nouv_grille=genere(nouv_grille)
        affichage_grille(nouv_grille)
        while not arret(nouv_grille):
            vers=input("choisir: l=gauche, r=droite, u=haut, d=bas: ")
            while not vers in 'lrud':
                vers=input("choisir: l=gauche, r=droite, u=haut, d=bas: ")
            if vers=='l':
                nouv_grille=deplacer_gauche(nouv_grille)
            elif vers=='r':
                nouv_grille=deplacer_droite(nouv_grille)
            elif vers=='u':
                nouv_grille=deplacer_haut(nouv_grille)
            elif vers=='d':
                nouv_grille=deplacer_bas(nouv_grille)
            nouv_grille=genere(nouv_grille)
            affichage_grille(nouv_grille)
        print("Joue Terminer")
    else:
        print("A Bientot")
            
 
if __name__ == '__main__':
    jouer()
   