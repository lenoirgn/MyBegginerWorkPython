# Compléter ici (noms, groupe, contenu fichier, date)
# Mamadou Radjaye sow MI23, Le traite de Binairo ,le 28/11/2025
#
#
#
# Ne pas supprimer cette ligne. <trace>binairo.py</trace>


####################
# Jeu du Binairo
####################
from copy import deepcopy


#Affichage

def affiche_motif():
    """ Affiche le motif
    Précondition :
    Exemple(s) :
    $$$ 
    """
    print('+---+---+---+---+')
def affiche_barre(i:int,j:int,k:int,l:int):
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
def afficher_menu():
    print("\n===== MENU NIVEAU BINAIRO =====")
    print("1 - Niveau facile")
    print("2 - Niveau moyen")
    print("3 - Niveau difficile")
    print("===============================")  
# Saisie
def saisie_coordonne()->list[int]:
    """ Saisie les coordonne de la case ( ligne et colonne)

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    indice_ligne=int(input(" Entrer l'indice de la ligne: "))
    while indice_ligne>=4:
         indice_ligne=int(input(" Entrer l'indice de la ligne(0 a 3): "))
         
    indice_col=int(input(" Entrer l'indice de la colonne: "))
    while indice_col>=4:
        indice_col=int(input(" Entrer l'indice de la colonne(0 a 3): "))
        
    return [indice_ligne,indice_col]


# Analyse et traitement

def comptage(liste:list[str],carac:str)->int:
    """Renvoie le nombre de occurrence de carac 

    Précondition : 
    Exemple(s) :
    $$$ comptage(['d','x','d','c','d'],'d')
    3
    $$$ comptage(['d','x','d','c','d'],'a')
    0
    $$$ comptage([],'a')
    0
    """
    compt=0
    for car in liste:
        if car==carac:
            compt+=1
    return compt

def est_egal(grille:list[list[str]],i:int)->bool:
    """ Renvoie True si le nombre de 0 et de 1 sont egale

    Précondition : 
    Exemple(s) :
    $$$ est_egal([['1','1','0','1'],['0','1','1','1'],['1','0','0','1'],['1','1','1','0']],0)
    False
    $$$ est_egal([['1','1','0','1'],['0','1','1','1'],['1','0','0','1'],['1','1','1','0']],2)
    True
    $$$ est_egal([['1','','0',''],['0','1','1','1'],['1','0','0','1'],['1','1','1','0']],0)
    True
    $$$ est_egal([['1','1','0',''],['0','1','1','1'],['1','0','0','1'],['1','1','1','0']],0)
    False
    
    """
    return comptage(grille[i],'0')== comptage(grille[i],'1')
    
    
    
def identique_droite(grille:list[list[str]],i:int,j:int)-> bool:
    """ Renvoie True si l'element a droite est identique a la case indexer

    Précondition : 
    Exemple(s) :
    $$$ identique_droite([['1','1','0','1'],['0','1','1','1'],['1','0','0','1'],['1','1','1','0']],1,2)
    True
    $$$ identique_droite([['1','1','0','1'],['0','1','0','0'],['1','0','1','1'],['1','0','1','1']],2,1)
    False
    $$$ identique_droite([['1','0','1','0'],['1','1','1','1'],['0','1','0','1'],['1','0','1','0']],0,3)
    False
    $$$ identique_droite([['0','1','1','1'],['1','0','1','0'],['1','1','0','1'],['1','1','0','0']],3,0)
    True
    $$$ identique_droite([['','1','0','1'],['1','','1','0'],['1','1','','1'],['0','','','']],3,1)
    False
    """
    if j+1<len(grille[i]):
        if grille[i][j]!='' and grille[i][j]==grille[i][j+1]:
            return True
    return False

def identique_gauche(grille:list[list[str]],i:int,j:int)-> bool:
    """ Renvoie True si l'element a gauche est identique a la case indexer
 

    Précondition : 
    Exemple(s) :
    $$$ identique_gauche([['1','1','0','1'],['0','1','1','1'],['1','0','0','1'],['1','1','1','0']],1,2)
    True
    $$$ identique_gauche([['1','1','0','1'],['0','1','0','0'],['1','0','1','1'],['1','0','1','1']],2,0)
    False
    $$$ identique_gauche([['1','0','1','0'],['1','1','1','1'],['0','1','0','1'],['1','0','1','0']],3,1)
    False
    $$$ identique_gauche([['0','1','1','1'],['1','0','1','0'],['1','1','0','0'],['1','1','0','0']],2,3)
    True
    $$$ identique_gauche([['','1','0','1'],['1','','1','0'],['1','1','','1'],['0','','','']],3,2)
    False
    """
    if j-1>=0:
        if grille[i][j]!='' and grille[i][j]==grille[i][j-1]:
            return True
    return False
    
def identique_haut(grille:list[list[str]],i:int,j:int)->bool:
    """ Renvoie True si l'element en haut est identique a la case indexer

    Précondition : 
    Exemple(s) :
    $$$ identique_haut([['X','','X',''],['O','','X','O'],['X','','X','O'],['O','','X','O']],1,2)
    True
    $$$ identique_haut([['X','','X',''],['O','','X',''],['X','','X','O'],['O','','X','O']],3,3)
    True
    $$$ identique_haut([['X','','X',''],['O','','X',''],['X','','X','O'],['O','','X','O']],1,0)
    False
    $$$ identique_haut([['X','','X',''],['O','','X',''],['X','','X','O'],['O','','X','O']],0,0)
    False
    $$$ identique_haut([['X','','X',''],['O','','X',''],['X','','X','O'],['O','','X','O']],1,1)
    False
    """
    if i-1>=0:
        if grille[i][j]!='' and grille[i][j]==grille[i-1][j]:
            return True
        
    return False

def identique_bas(grille:list[list[str]],i:int,j:int)->bool:
    """ Renvoie True si l'element en bas est identique a la case indexer

    Précondition : 
    Exemple(s) :
    $$$ identique_bas([['X','','X',''],['O','','X','O'],['X','','X','O'],['O','','X','O']],0,2)
    True
    $$$ identique_bas([['X','','X',''],['O','','X',''],['X','','X','O'],['O','','X','O']],1,2)
    True
    $$$ identique_bas([['X','','X',''],['O','','X',''],['X','','X','O'],['O','','X','O']],1,0)
    False
    $$$ identique_bas([['X','','X',''],['O','','X',''],['X','','X','O'],['O','','X','O']],3,0)
    False
    $$$ identique_bas([['X','','X',''],['O','','X',''],['X','','X','O'],['O','','X','O']],1,1)
    False
    """
    if i+1<len(grille):
        if grille[i][j]!='' and grille[i][j]==grille[i+1][j]:
            return True
        
    return False
    
def alentour_identique(grille:list[list[str]],i:int,j:int)->bool:
    """ Renvoie True si au moins deux case a l'alentour sont identique a la case selectionner 
    Précondition : 
    Exemple(s) :
    $$$ alentour_identique([['X','','X',''],['O','','X','O'],['X','','X','O'],['O','','X','O']],1,2)
    True
    $$$ alentour_identique([['X','','X',''],['O','O','X',''],['X','','X','O'],['O','','X','O']],1,0)
    False
    $$$ alentour_identique([['X','','X',''],['X','','X',''],['X','','X','O'],['O','','X','O']],2,0)
    False
    $$$ alentour_identique([['X','','X',''],['O','','X',''],['X','','X','O'],['O','','X','O']],3,0)
    False
    $$$ alentour_identique([['X','','X',''],['X','','X',''],['X','','X','O'],['O','','X','O']],0,0)
    False
    """
    return   (identique_bas(grille,i,j) and identique_haut(grille,i,j)) or (identique_droite(grille,i,j) and identique_gauche(grille,i,j))

def est_identique_audela(grille:list[list[str]],i:int,j:int)->bool:
    """ Renvoi si au moins deux case suivante de la case a l'alentour sont identique

    Précondition : 
    Exemple(s) :
    $$$ est_identique_audela([['X','X','X',''],['O','','X','O'],['X','','X','O'],['O','','X','O']],1,1)
    False
    $$$ est_identique_audela([['X','','X',''],['X','','X',''],['X','','X','O'],['X','','X','O']],1,0)
    True
    $$$ est_identique_audela([['O','','X',''],['X','','X',''],['X','','X','O'],['X','','','O']],2,2)
    True
    $$$ est_identique_audela([['X','','X',''],['O','','X',''],['O','','X','O'],['O','','X','O']],3,0)
    True
    $$$ est_identique_audela([['X','','X',''],['O','','X',''],['X','','X','O'],['X','','X','O']],2,0)
    False
    $$$ est_identique_audela([['X','','X',''],['X','','X',''],['X','','X','O'],['O','','X','O']],0,0)
    True
    $$$ est_identique_audela([['O','O','O',''],['X','','X',''],['X','','X','O'],['O','','X','O']],0,2)
    True
    $$$ est_identique_audela([['0','1','0','1'], ['1','0','1','0'], ['0','0','1','1'], ['1','1','0','0']],2,2)
    False

    """
    identique=False
    if grille[i][j]!='' and j+1 < len(grille[i]) and j+2 < len(grille[i]) and  grille[i][j]==grille[i][j+1]==grille[i][j+2]:
        identique=True
    elif grille[i][j]!='' and j-2>=0 and j-1>=0 and  grille[i][j-2]==grille[i][j-1]==grille[i][j]:
        identique=True
    elif grille[i][j]!='' and i+1 < len(grille) and i+2 < len(grille)  and grille[i][j]==grille[i+1][j]==grille[i+2][j]:
        identique=True
    elif grille[i][j]!='' and i-2>=0 and i-1>=0 and grille[i-2][j]==grille[i-1][j]==grille[i][j]:
        identique=True
    return identique
  
 
def position_trouver(grille:list[list[str]],i:int,j:int)->bool:
    """ Renvoi True si les case a l'alentour sont identique ou ceux suivent

    Précondition : 
    Exemple(s) :
    $$$ position_trouver([['X','','X',''],['O','','X',''],['O','','X','O'],['O','','X','O']],3,0)
    True
    $$$ position_trouver([['X','X','X',''],['O','','X',''],['O','','X','O'],['O','','X','O']],0,1)
    True
    $$$ position_trouver([['X','','X',''],['O','','X',''],['O','','X','O'],['O','','X','O']],2,3)
    False 
    $$$ position_trouver([['0','1','0','1'], ['1','0','1','0'], ['0','0','1','1'], ['1','1','0','0']],2,3)
    False
    $$$ position_trouver([['0','1','0','1'], ['1','0','1','0'], ['0','0','1','1'], ['1','1','0','0']],2,2)
    False
    """
    return  alentour_identique(grille,i,j) or est_identique_audela(grille,i,j)
        

    
def est_horiz_identique(grille:list[list[str]])->bool:
    """ Renvoie True si une ligne est identique a l'autre

    Précondition : 
    Exemple(s) :
    $$$ est_horiz_identique([['X','X','X','X'],['O','','O','X'],['X','O','O','X'],['O','','O','X']])
    False
    $$$ est_horiz_identique([['X','O','O','X'],['O','O','O','O'],['X','','O','X'],['O','O','O','O']])
    True
    $$$ est_horiz_identique([['X','O','',''],['X','','O','X'],['','X','O','X'],['X','O','','X']])
    False
    $$$ est_horiz_identique([['','','',''],['','','',''],['','','',''],['','','','']])
    False
    """
    for i in range(4):
        for j in range(i+1,4):
            if not '' in grille[i]:
                if grille[i]==grille[j]:
                    return True
        
    return False 
           
def est_verti_identique(grille:list[list[str]])->bool:
    """  Renvoie True si une colonne est identique a l'autre 

    Précondition : 
    Exemple(s) :
    $$$ est_verti_identique([['0','0','1','0'],['1','1','0','1'],['0','0','1','0'],['1','1','0','1']])
    True
    $$$ est_verti_identique([['0','0','1','1'],['1','1','0','0'],['0','1','0','1'],['1','0','1','0']])
    False
    $$$ est_verti_identique([['0','1','0','1'],['1','0','1','0'],['0','1','0','1'],['1','0','1','0']])
    True
    $$$ est_verti_identique([['0','1','1','O'], ['0','1','0','1'], ['1','0','1','0'], ['1','0','1','0']])
    False
    $$$ est_verti_identique([['','0','','0'], ['0','0','1','0'], ['0','1','0','1'], ['','','','0']])
    False
    """
    liste_temp=[]
    grille_temp=[]
    for i in range(4):
        for j in range(4):
            liste_temp.append(grille[j][i])
        grille_temp.append(liste_temp)
        liste_temp=[]
    
    if est_horiz_identique(grille_temp):
        return True
    return False
 


def identique_alignement(grille:list[list[str]])->bool:
    """ Renvoie True si au moins un alignement est vrai

    Précondition : 
    Exemple(s) :
    $$$ identique_alignement([['0','1','1','O'], ['0','1','0','1'], ['1','0','1',''], ['1','0','1','0']])
    False
    $$$ identique_alignement([['X','O','',''],['X','','O','X'],['','X','O','X'],['X','O','','X']])
    False
    $$$ identique_alignement([['X','O','O','X'],['O','O','O','O'],['X','','O','X'],['O','O','O','O']])
    True
    $$$ identique_alignement([['0','1','0','1'],['1','0','1','0'],['0','1','0','1'],['1','0','1','0']])
    True
    $$$ identique_alignement([['0','1','0','1'], ['1','0','1','0'], ['0','1','0','1'], ['1','0','1','0']])
    True
    """
    return   est_horiz_identique(grille) or est_verti_identique(grille)
    

   
def grille_vide() -> list[list[str]]:
    """ Renvoie une grille initialise

    Précondition :
    Exemple(s) :
    $$$ 
    """
    grille = []
    ligne = ["","","",""]
    for i in range(4):
        grille.append(ligne.copy())
    return grille 

    
def init_grille(fichier:str,grille:list[list[str]])->list[list[str]]:
    """ Initialise une grille

    Précondition : 
    Exemple(s) :
    $$$ init_grille('init_config.txt',[['','','',''],['','','',''],['','','',''],['','','','']])
    [['0','0','',''],['0','','',''],['','1','',''],['','','','']]
    """
    res=deepcopy(grille)
    with open(fichier,'r') as f:
        List_ligne=f.readlines()
        for ligne in List_ligne:
            temp=ligne.rstrip()
            val=temp.split(';')
            num_ligne=int(val[0])
            num_col=int(val[1])
            res[num_ligne][num_col]=val[2]
            
    return res

def inchangeables(fichier:str)->list[list[str]]:
    """ Renvoie les cases inchangeables

    Précondition : 
    Exemple(s) :
    $$$ inchangeables('init_config.txt')
    [[0,0],[0,1],[1,0],[2,1]]
    """
    lres=[]
    with open(fichier,'r') as f:
        List_ligne=f.readlines()
        for ligne in List_ligne:
            temp=ligne.rstrip()
            val=temp.split(';')
            list_temp=[int(val[0]),int(val[1])]
            lres.append(list_temp)
    return lres
            
def est_plein(grille:list[list[str]]) -> bool:
    """ Renvoie True si la grille est plein

    Précondition : 
    Exemple(s) :
    $$$ est_plein([['X','O','O','X'],['O','O','O','O'],['X','X','O','X'],['O','X','O','X']])
    True
    $$$ est_plein([['X','O','O','X'],['O','O','O','O'],['X','X','O','X'],['O','X','O','']])
    False
    $$$ est_plein([['X','O','O','X'],['O','O','O','O'],['X','','O','X'],['','','O','']])
    False
    """
    for ligne in grille:
        if '' in ligne:
            return False
    return True
            
def mise_Ajour(grille:list[list[str]],i:int,j:int,choix:str)->list[list[str]]:
    """ Renvoie une grille mise a jour

    Précondition : 
    Exemple(s) :
    $$$ g= mise_Ajour([['','O','',''],['','','O','X'],['X','','O','X'],['X','O','O','X']],0,0,'X')
    $$$ g
    [['X','O','',''],['','','O','X'],['X','','O','X'],['X','O','O','X']]
    $$$ g= mise_Ajour([['X','O','',''],['','','O','X'],['X','','O','X'],['X','O','O','X']],2,1,'O')
    $$$ g
    [['X','O','',''],['','','O','X'],['X','O','O','X'],['X','O','O','X']]
    """
    nouv_grille=deepcopy(grille)
    nouv_grille[i][j]=choix
    return nouv_grille
           
def a_gagner(grille:list[list[str]])->bool:
    """ Renvoie True si le joueur a gagne
    Précondition : 
    Exemple(s) :
    $$$ a_gagner([['0','1','0','1'], ['1','0','1','0'], ['0','0','1','1'], ['1','1','0','0']])
    True
    $$$ a_gagner([['0','0','1','1'], ['1','1','0','0'], ['0','1','1','0'], ['1','0','0','1']])
    True
    $$$ a_gagner([['0','0','0','1'], ['1','0','1','0'], ['0','0','1','1'], ['1','1','0','0']])
    False
    $$$ a_gagner([['0','1','0','1'], ['1','0','1','0'], ['0','1','0','1'], ['1','0','1','0']])
    False
    $$$ a_gagner([['1','0','0','1'], ['0','1','1','0'], ['0','1','0','1'], ['1','0','0','0']])
    False
    $$$ a_gagner([['1','0','0','1'], ['','1','',''], ['0','1','0','1'], ['1','0','1','0']])
    False
    """
    
    if identique_alignement(grille):
        return False
    for i in range(4):
       for j in range(4):
             if position_trouver(grille,i,j):
               return False
       if not est_egal(grille,i):
            return False
    return True
def choix_file(liste:list[str],entier:int)->str:
    """
    Précondition : 
    Exemple(s) :
    $$$ choix_file(['bah','blabla','blablakar'],1)
    'bah'
    $$$ choix_file(['bah','blabla','blablakar'],3)
    'blablakar'
    """
    fichier=''
    if entier == 1:
        fichier=liste[0]
    elif entier == 2:
        fichier=liste[1]
    elif entier == 3:
        fichier=liste[2]
    return fichier 
      
    
        
def jouer():
    grille=grille_vide()
    affichage_grille(grille)
    liste_file=['init_config.txt','config_moyen.txt','config_hard.txt']
    avis=input("Voulez-vous jouer Y/N: ")
    if avis=='Y':
        afficher_menu()
        choix_niveau=int(input("Entrez le niveau de jeu: "))
        while choix_niveau<1 or choix_niveau>3:
            choix_niveau=int(input("Entrez le niveau de jeu: "))
            
        fichier=choix_file(liste_file,choix_niveau)
        nouvel_grille=init_grille(fichier,grille)
        inchangeable=inchangeables('init_config.txt')
        affichage_grille(nouvel_grille)
        while (not est_plein(nouvel_grille)) or (not a_gagner(nouvel_grille)):
            list_coordonne=saisie_coordonne()
            while list_coordonne in inchangeable:
                print('vous ne pouvez pas changez cette case')
                list_coordonne=saisie_coordonne()
            choix=input("Entrer 0 ou 1: ")
            while choix!='0'and choix!='1':
                choix=input("Entrer 0 ou 1: ")
            nouvel_grille=mise_Ajour(nouvel_grille,list_coordonne[0],list_coordonne[1],choix)
            affichage_grille(nouvel_grille)
            if not est_egal(nouvel_grille,list_coordonne[0]):
                print(f'A la ligne {list_coordonne[0]}, le nombre de 0 et 1 ne sont pas egaux !')
            if identique_alignement(nouvel_grille):
                print("Alignement identique trouver !")
            if position_trouver(nouvel_grille,list_coordonne[0],list_coordonne[1]):
                print(f"il  3 '{choix}' aligne ")

   
        print("Vous avez gagner !")
    else:
        print("A la prochaine")
 
 
if __name__ == '__main__':
   jouer() 