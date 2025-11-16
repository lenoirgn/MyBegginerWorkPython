# Compléter ici (noms, groupe, contenu fichier, date)
#Mamadou Radjaye sow MI23 le 14/11/025
#
#
#
# Ne pas supprimer cette ligne. <trace>parcours_interrompus_simples.py</trace>

#################################
# Parcours interrompus simples d'itérables avec une boucle while / for
#################################


def contient_negatif_for(lentier:list[int]):
    """ Renvoie True ssi cette liste contient un entier négatif
    Précondition : 
    Exemple(s) :
    $$$ contient_negatif_for([-2,3])
    True
    $$$ contient_negatif_for([2,3,-2])
    True
    $$$ contient_negatif_for([2,-3,2])
    True
    $$$ contient_negatif_for([2,3,2])
    False
    $$$ contient_negatif_for([])
    False
    """
    for entier in lentier:
        if entier <0:
            return True
    return False
    


def contient_negatif_while(lentier:list[int]):
    """ Renvoie True ssi cette liste contient un entier négatif
    Précondition : 
    Exemple(s) :
    $$$ contient_negatif_while([-2,3])
    True
    $$$ contient_negatif_while([2,3,-2])
    True
    $$$ contient_negatif_while([2,-3,2])
    True
    $$$ contient_negatif_while([2,3,2])
    False
    $$$ contient_negatif_while([])
    False
    """
    if lentier==[]:
        return False
    i=0
    while i<len(lentier) and lentier[i]>=0:
        i+=1
    return i<len(lentier) 

def toutes_longueurs_impaires_while(chaine:list[str]):
    """ renvoient True ssi les longueurs de toutes les
    chaînes de la liste sont impaires

    Précondition : 
    Exemple(s) :
    $$$ toutes_longueurs_impaires_while(['b', 'bce', 'e'])
    True
    $$$ toutes_longueurs_impaires_while(['b', 'bc', 'e'])
    False
    $$$ toutes_longueurs_impaires_while(['b', 'bc', 'ec'])
    False
    $$$ toutes_longueurs_impaires_while(['bx', 'bc', 'e'])
    False
    $$$ toutes_longueurs_impaires_while(['bx', 'b', 'eb'])
    False
    $$$ toutes_longueurs_impaires_while([])
    True
    """
    i=0
    while i<len(chaine) and not len(chaine[i])%2==0:
        i+=1
        
    return i==len(chaine)
    

def toutes_longueurs_impaires_for(lchaine:list[str])->bool:
    """ renvoient True ssi les longueurs de toutes les
    chaînes de la liste sont impaires

    Précondition : 
    Exemple(s) :
    $$$ toutes_longueurs_impaires_for(['b', 'bce', 'e'])
    True
    $$$ toutes_longueurs_impaires_for(['b', 'bc', 'e'])
    False
    $$$ toutes_longueurs_impaires_for(['b', 'bc', 'ec'])
    False
    $$$ toutes_longueurs_impaires_for(['bx', 'bc', 'e'])
    False
    $$$ toutes_longueurs_impaires_for(['bx', 'b', 'eb'])
    False
    $$$ toutes_longueurs_impaires_for([])
    True
    """
    for chaine in lchaine:
        if len(chaine)%2==0:
            return False
    return True
        


def contient_chiffre_ou_minuscule_while(chaine:str)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ contient_chiffre_ou_minuscule_while('dje')
    True
    $$$ contient_chiffre_ou_minuscule_while('TH6j')
    True
    $$$ contient_chiffre_ou_minuscule_while('TH')
    False
    $$$ contient_chiffre_ou_minuscule_while('TH')
    False
    $$$ contient_chiffre_ou_minuscule_while('THj')
    True
    $$$ contient_chiffre_ou_minuscule_while('')
    False
    """
    i=0
    while i<len(chaine) and not (chaine[i].isdigit() or chaine[i].islower()):
        i+=1
    return  i<len(chaine)
        
    


def contient_chiffre_ou_minuscule_for(chaine:str)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ contient_chiffre_ou_minuscule_for('dje')
    True
    $$$ contient_chiffre_ou_minuscule_for('TH6j')
    True
    $$$ contient_chiffre_ou_minuscule_for('TH')
    False
    $$$ contient_chiffre_ou_minuscule_for('TH')
    False
    $$$ contient_chiffre_ou_minuscule_for('THj')
    True
    $$$ contient_chiffre_ou_minuscule_for('')
    False 
    """
    for carac in chaine:
        if carac.isdigit() or carac.islower():
            return True
    return False
    


def indice_positif_while(lentier:list[int])->int:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ indice_positif_while([2,3,4])
    0
    $$$ indice_positif_while([-2,3,-4])
    1
    $$$ indice_positif_while([-2,-3,4])
    2
    $$$ indice_positif_while([-2,-3,-4])
    3
    """
    i=0
    res=0
    while i<len(lentier) and  lentier[i]<0:
        i+=1
        if i==len(lentier):
            res=len(lentier)
        else:
            res=i
    return res
    

def indice_positif_for(lentier:list[int])->int:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ indice_positif_for([2,3,4])
    0
    $$$ indice_positif_for([-2,3,-4])
    1
    $$$ indice_positif_for([-2,-3,4])
    2
    $$$ indice_positif_for([-2,-3,-4])
    3 
    """
    i=0
    for entier in lentier:
        
        if entier >0 :
            return i
        else:
            i+=1
    return len(lentier)

def contient_nb_occurrences_ou_plus_while(chaine : str, c : str, nb : int)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ contient_nb_occurrences_ou_plus_while('mandeaa','a',2)
    True
    $$$ contient_nb_occurrences_ou_plus_while('amande','n',4)
    False
    $$$ contient_nb_occurrences_ou_plus_while('amande','e',1)
    True
    $$$ contient_nb_occurrences_ou_plus_while('amande','e',1)
    True
    """
    i=0
    nb_occu=0
    while i<len(chaine) and nb_occu<nb:
        
        if chaine[i]==c:
            nb_occu+=1
        i+=1
    return i<len(chaine) or nb_occu==nb

def contient_nb_occurrences_ou_plus_for(chaine : str, c : str, nb : int):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ contient_nb_occurrences_ou_plus_for('mandeaa','a',2)
    True
    $$$ contient_nb_occurrences_ou_plus_for('amande','n',4)
    False
    $$$ contient_nb_occurrences_ou_plus_for('amande','e',1)
    True
    $$$ contient_nb_occurrences_ou_plus_for('amande','e',1)
    True 
    """
    nb_occu=0
    for carac in chaine:
        if carac==c:
            nb_occu+=1
            if nb_occu==nb:
                return True
    return False
            
    
