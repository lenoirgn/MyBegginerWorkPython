def grille_vide(entier:int)->list[list[str]]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    ligne=['']*entier
    grille=[]
    for i in range(entier):
        grille.append(ligne.copy())
    return grille
from copy import deepcopy
def init_grille(fichier:str)->list[list[str]]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    with open(fichier,'r') as f:
        nb=f.readline()
        liste=f.readlines()
    grille=grille_vide(int(nb))
    nouv_grille=deepcopy(grille)
    print(liste)
    for elet in liste:
        elet=elet.split(',')
        nouv_grille[int(elet[0])][int(elet[1])]=elet[2].strip()
    return nouv_grille
def positionne_symbole(grille:list[list[str]],i:int,j:int,carac:str)->list[list[str]]:
    """
    Précondition : 
    Exemple(s) :
    $$$ 
    """
    nouv_grille=deepcopy(grille)
    nouv_grille[i][j]=carac
    return nouv_grille
    
def ecrire_coup(i:int,j:int,carac:str):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    with open("grille_test.txt",'w') as f:
        f.writelines([str(i),',',str(j),',',carac])
        
def est_ligne_incomplete(liste:list[str])->bool:
     """ 

     Précondition : 
     Exemple(s) :
     $$$ est_ligne_incomplete(['d','a','v',''])
     True
     $$$ est_ligne_incomplete(['d','a','v','d'])
     False
     """
     i=0
     while i<len(liste) and liste[i]!='':
         i+=1
     return i<len(liste)
         

def est_pleine(liste:list[str])->bool:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ est_pleine(['d','a','v',''])
    False
    $$$ est_pleine(['d','a','v','d'])
    True
    """
    for elt in liste:
         if elt=='':
            return False
    return True 
    
def saisie_symbole():
    """ 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    valeur=int(input("Entrer 1 ou 0: "))
    while valeur !=1 and valeur !=0:
        print("Incorrect")
        valeur=int(input("Entrer 1 ou 0: "))
import string
from random import choice
def tirage_lettres(nb_v:int,nb_con:int)->str:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    alphabet=string.ascii_lowercase
    voyelle= "aeiouy"
    comp_v=0
    comp_c=0
    res=''
    while comp_v<nb_v or comp_c < nb_con :
        temp=choice(alphabet)
        
        if temp in voyelle:
             if comp_v < nb_v:
                comp_v += 1
                res+=temp       
        else:
            if comp_c < nb_con:
                comp_c += 1
                res+=temp          
    return res
            
def calcule_score(liste1:list[tuple[str,int]],liste2:list[str])->int:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ calcule_score([('k', 10), ('i', 1), ('w', 10), ('i', 1)], ['ld', '', '','lt'])
    10*2 + 1 + 10 + 1 * 3
    """
    res=0
    for i in range(len(liste2)):
        if liste2[i]=='ld':
            liste2[i]='2'
        elif liste2[i]=='lt':
            liste2[i]='3'
        elif liste2[i]=='':
            liste2[i]='1'
        res+=liste1[i][1]*int(liste2[i])
    return res
    
def paires(chaine:str)->list[str]:
    """ 
    Précondition : 
    Exemple(s) :
    $$$ paires('note')
    ['no', 'on', 'nt', 'tn', 'ne', 'en', 'ot', 'to', 'oe', 'eo', 'te', 'et']
    """
    paires = []
    n = len(chaine)

    for i in range(n):
        for j in range(i + 1, n):
            paires.append(chaine[i] + chaine[j])
            paires.append(chaine[j] + chaine[i])
    lres=[]
    for i in range(len(paires)):
        if not paires[i] in paires[i+1:]:
            lres.append(paires[i])
    return lres
# cette methode prend du temps et beaucoup de ram
#     lres=[]
#     while len(lres)<len(chaine)*(len(chaine)-1):
#         temp=''
#         while len(temp)<2:
#             alea=choice(chaine)
#             if not alea in temp:
#                 temp+=alea
#         if not temp in lres:
#             lres.append(temp) 
#     return lres

        
def a_n_consonnes_doublees_ou_plus (chaine:str,entier:int)->bool:
    """
    Précondition : 
    Exemple(s) :
    $$$ a_n_consonnes_doublees_ou_plus ("ressasser",2)
    True
    $$$ a_n_consonnes_doublees_ou_plus ("incessamment ",2)
    True
    $$$ a_n_consonnes_doublees_ou_plus ("mamadou",2)
    False
    $$$ a_n_consonnes_doublees_ou_plus ("incessamment",3)
    False
    """
    comp=0
    for i in range(len(chaine)-1):
        if chaine[i]==chaine[i+1]:
            comp+=1
    if comp<entier:
        return False
    return True
    
    
    
    
    
    