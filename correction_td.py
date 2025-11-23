def foo1(liste:list[int]) -> bool:
    """ 
    Précondition : 
    Exemple(s) :
    $$$ foo1([-2,3,0])
    True
    $$$ foo1([-2,-3,0])
    True
    $$$ foo1([-2,-3])
    False
    $$$ foo1([])
    False
    """
    
    for elem in liste:
        if elem >= 0:
            return True
    
    return False

def foo4(liste:list[int]) -> bool:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ foo4([-2,3,0])
    True
    $$$ foo4([-2,-3,0])
    True
    $$$ foo4([-2,-3])
    False
    $$$ foo4([])
    False 
    """
    
    i = 0
    while i < len(liste) and liste[i] < 0:
        i = i + 1
    return i < len(liste)

def est_premier_naif_for(entier:int)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ est_premier_naif_for(9)
    False
    $$$ est_premier_naif_for(7)
    True
    """
    if entier<2:
        return False
    for i in range(2,entier):
        if entier%i==0:
            return False
    return True
            
def  est_premier_naif_while(entier:int)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ est_premier_naif_while(9)
    False
    $$$ est_premier_naif_while(7)
    True 
    """
    i=2
    while i<entier and entier%i!=0:
        i+=1
    return i>=entier
   
def prédicat_au_moins_un_premier_for(interval:range)->bool:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ prédicat_au_moins_un_premier_for(range(4))
    True
    $$$ prédicat_au_moins_un_premier_for(range(8,11))
    False    
    
    """
    for i in interval:
        if est_premier_naif_for(i):
            return True
    return False

def prédicat_au_moins_un_premier_while(interval:range)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ prédicat_au_moins_un_premier_while(range(4))
    True
    $$$ prédicat_au_moins_un_premier_while(range(8,11))
    False  
    """
    i=0
    while i<len(interval) and not est_premier_naif_while(interval[i]):
        i+=1
    return i<len(interval)
from random import randint 
def genere_binaire(entier:int)->str:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    res=''
    comp0=0
    comp1=0
    i=0
    while comp0<entier and comp1<entier:
        res+=str(randint(0,1))
        if randint(0,1)==0:
            comp0+=1
        else:
            comp1+=1
            
    return res 
def apparait(mot:str,texte:str)->bool:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ apparait('chat','cheminemant')
    True
    $$$ apparait('chat','chemin')
    False
    """
    i=0
    for car in texte:
        if i < len(mot) and car == mot[i]:
            i+=1
    return i==len(mot)
def prefixe_somme(lentier:list[int],entier:int)->list[int]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ prefixe_somme([1, 2, 3], 1)
    [1]
    $$$ prefixe_somme([1, 2, 3], 4)
    [1, 2, 3]
    $$$ prefixe_somme([1, 2, 3], 10)
    [1, 2, 3]
    """
    somme=0
    i=0
    lres=[]
    while i<len(lentier) and somme<entier:
        lres.append(lentier[i])
        somme+=lentier[i]
        i+=1
    return lres
def somme_vaut_n(lentier:list[int],entier:int)->bool:
     """

     Précondition : 
     Exemple(s) :
     $$$ somme_vaut_n([1, 2, 3], 6)
     True
     $$$ somme_vaut_n([1, 2, 3,9], 6)
     False
     $$$ somme_vaut_n([1, 5, 2], 3)
     False
     $$$ somme_vaut_n([1, 1, 1], 6)
     False
     $$$ somme_vaut_n([1, 5, 1], 6)
     False
     $$$ somme_vaut_n([], 0)
     True
     $$$ somme_vaut_n([], 2)
     False
     """
     som=0
     i=0
     if lentier==[] and entier ==0:
         return True
     while i<len(lentier) and som<=entier :
         som+=lentier[i]
         i+=1
     return  som==entier 

def est_inferieure_strict(lentier1:list[int],lentier2:list[int])->bool:
    """ renvoie True ssi liste1 < liste2

    Précondition : 
    Exemple(s) :
    $$$ est_inferieure_strict([2, 5, 4, 6, 7],[5])
    True
    $$$ est_inferieure_strict([5, 5, 2] , [5, 5, 7])
    True
    $$$ est_inferieure_strict([5, 5, 2] , [5, 5, 1])
    False
    $$$ est_inferieure_strict([5, 6] , [5, 6, 7])
    True
    """
    i=0
    while i<min(len(lentier1),len(lentier2)) and lentier1[i]==lentier2[i]:
        i+=1
    if i == len(lentier1) and i == len(lentier2):
        return False
    elif i == len(lentier1):
        return True
    elif i == len(lentier2):
        return False
    else:
        
        return lentier1[i] < lentier2[i]
        