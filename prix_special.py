def est_prix_special(entier:int):
    """

    Précondition : 
    Exemple(s) :
    $$$ est_prix_special(5)
    False
    $$$ est_prix_special(15)
    True
    $$$ est_prix_special(100)
    False
    $$$ est_prix_special(90)
    True
    $$$ est_prix_special(61)
    False
    """
    return  entier%5==0 and 10<entier and entier<=90
def nombre_prix_speciaux(lentier:list[int]):
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ nombre_prix_speciaux([5, 15, 100, 90, 61])
    2
    """
    compt=0
    for entier in lentier:
        if est_prix_special(entier):
            compt+=1
    return compt

def cout_panier(liste_quantite:list[int],liste_prix:list[int])->int:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ cout_panier([15], [2])
    30
    $$$ cout_panier([15, 10, 2], [2, 3, 2])
    64
    """
    prix_totale=0
    for i in range(len(liste_prix)):
        prix_totale+=liste_quantite[i]*liste_prix[i]
    return prix_totale

def prix_reduit_panier(liste_quantite:list[int],liste_prix:list[int]):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ prix_reduit_panier([1,1,1,1],[15,90,2,25])
    118.8
    """
    
    if nombre_prix_speciaux(liste_prix)>=3:
        prix_panier=cout_panier(liste_quantite,liste_prix)-cout_panier(liste_quantite,liste_prix)*0.1
    else:
        prix_panier=cout_panier(liste_quantite,liste_prix)
    return prix_panier

#lance de
from random import randint,choice
def lancer():
    """ 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    return randint(1,6)

def numero_lancer_premier_6():
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    compt=1
    while lancer()!=6:
        
        compt+=1
    return compt 
    
# Nombre complémentaire
def puissance(base:int,exp:int):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ puissance(10,3)
    1000
    $$$ puissance(10,0)
    1
    """
    return base**exp

def nb_chiffres(entier:int):
    """
    Précondition : 
    Exemple(s) :
    $$$ nb_chiffres(4)
    1
    $$$ nb_chiffres(0)
    1
    $$$ nb_chiffres(489)
    3
    """
    compt=1
    divi=entier//10
    if not entier ==0:
        while divi !=0:
            compt+=1
            divi=divi//10
    return compt
        
def complement(entier:int):
    """

    Précondition : 
    Exemple(s) :
    $$$ complement(791)
    209
    $$$ complement(0)
    10
    """
    return puissance(10,nb_chiffres(entier))-entier
    
#Devine le mot

def genere_minuscule():
    """ 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    return choice('abcdefghijklmnopqrstuvwxyz')
def genere_mot(n:int):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    mot=''
    for i in range(n):
        mot+=genere_minuscule()
    return mot 
def positions_lettres_differentes(chaine1:str,chaine2:str):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ positions_lettres_differentes('ahva', 'chat')
    [0, 2, 3]
    """
    lres=[]
    for i in range(len(chaine1)) :
        if chaine1[i]!=chaine2[i]:
            lres.append(i)
    return lres
def change_lettre_pos(chaine:str,carac:str,posi:int):
    """
    Précondition : 
    Exemple(s) :
    $$$ change_lettre_pos('ahva', 'a', 2)
    'ahaa' 
    """
    return chaine[:posi]+carac+chaine[posi+1:]

def devine_mot_limite(chaine:str,max_essai:int):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    
    mot=genere_mot(len(chaine))
    if mot != chaine:
        listPosi=positions_lettres_differentes(mot,chaine)
        while max_essai!=0:
            max_essai-=1
            lettre=genere_minuscule()
            for ele in listPosi:
                if chaine[ele]==lettre:
                    mot=change_lettre_pos(mot,lettre,ele)
                    listPosi=positions_lettres_differentes(mot,chaine)
                
    return mot    
            
        
        

