# Compléter ici (noms, groupe, contenu fichier, date)
# Mamadou Radjaye sow MI23 Traite de parcours interrompus synthese le 14/11/025
#
#
#
# Ne pas supprimer cette ligne. <trace>parcours_interrompus_synthese.py</trace>

#################################a
# Parcours moins simples interrompus d'itérables 
#################################a

def est_palindrome_sem9_while(chaine:str)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ est_palindrome_sem9_while('elle')
    True
    $$$ est_palindrome_sem9_while('ici')
    True
    $$$ est_palindrome_sem9_while('12261')
    False
    $$$ est_palindrome_sem9_while('kayak')
    True
    $$$ est_palindrome_sem9_while('dort')
    False
    
    """
    i=0
    inverse_indice=-1
    while i<len(chaine) and chaine[i]==chaine[inverse_indice]:
        i+=1
        inverse_indice-=1
    return i==len(chaine)

def est_palindrome_sem9_for(chaine):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ est_palindrome_sem9_for('elle')
    True
    $$$ est_palindrome_sem9_for('ici')
    True
    $$$ est_palindrome_sem9_for('12261')
    False
    $$$ est_palindrome_sem9_for('kayak')
    True
    $$$ est_palindrome_sem9_for('dort')
    False 
    """
    i=-1
    for carac in chaine:
        if carac!=chaine[i]:
            return False
        else:
             i-=1
    return True
            
    

def est_croissante_while(lentier:list[int])->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ est_croissante_while([1,2,3,6])
    True
    $$$ est_croissante_while([1,4,3,6])
    False
    $$$ est_croissante_while([1,2,3,0])
    False
    $$$ est_croissante_while([5,2,3,4])
    False
    """
    i=0
    while i<len(lentier)-1 and lentier[i]<lentier[i+1]:
        i+=1
    return i==len(lentier)-1
    


def est_croissante_for(lentier:list[int])->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ est_croissante_for([1,2,3,6])
    True
    $$$ est_croissante_for([1,4,3,6])
    False
    $$$ est_croissante_for([1,2,3,0])
    False
    $$$ est_croissante_for([5,2,3,4])
    False 
    """
    prec=lentier[0]
    for entier in lentier[1:]:
        if prec>=entier:
            return False
        prec=entier
    return True

def tous_differents_while(lentier:list[int])->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ tous_differents_while([1,2,3])
    True
    $$$ tous_differents_while([1,2,1])
    False
    $$$ tous_differents_while([1,2,2])
    False
    $$$ tous_differents_while([])
    True
    """
    if lentier==[]:
        return True
    i=0
    trouve_different=True
    while i<len(lentier) and trouve_different:
        for val in range(len(lentier)):
            if val!=i and lentier[i]==lentier[val]:
               trouve_different=False 
        i+=1
    return trouve_different
    


def tous_differents_for(lentier:list[int])->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ tous_differents_for([1,2,3])
    True
    $$$ tous_differents_for([1,2,1])
    False
    $$$ tous_differents_for([1,2,2])
    False
    $$$ tous_differents_for([])
    True 
    """
    
    
    for i in range(len(lentier)):
        for p in range(len(lentier)):
            if p!=i and lentier[i]==lentier[p]:
               return False
    return True 
       
   

def produit_vaut_n_while(liste: list[int], n: int):
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ produit_vaut_n_while([1,2,3],6)
    True
    $$$ produit_vaut_n_while([1,6,3],30)
    False
    $$$ produit_vaut_n_while([1,2,3],2)
    False
    """
    i=0
    prod=1
    while i<len(liste) and prod<=n:
        prod=prod*liste[i]
        i+=1
    return i<len(liste) or prod==n
        
def produit_vaut_n_for(liste: list[int], n: int)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ produit_vaut_n_for([2,2,3],12)
    True
    $$$ produit_vaut_n_for([1,6,3],30)
    False
    $$$ produit_vaut_n_for([1,2,3],2)
    False 
    """
    prod = 1
    for entier in liste:
        prod *= entier
        if prod > n:
            return False
    
    return prod == n

def suffixe_somme_while(liste : list[int], n : int)->list:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ suffixe_somme_while([2,2,3],5)
    [2,3]
    $$$ suffixe_somme_while([1,6,3],30)
    []
    $$$ suffixe_somme_while([1,2,3],2)
    [3]
    """
    lres = []
    som = 0
    i = len(liste) - 1   

    while i>=0 and som < n:
        lres.append(liste[i])   
        som += liste[i]
        i -= 1

    if som >= n:
        return lres[::-1]       
    else:
        return []
            
            

def suffixe_somme_for(liste : list[int], n : int)->list:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ suffixe_somme_for([2,2,3],5)
    [2,3]
    $$$ suffixe_somme_for([1,6,3],30)
    []
    $$$ suffixe_somme_for([1,2,3],2)
    [3] 
    """
    som=0
    lres=[]
    for entier in liste[::-1]:
        som+=entier
        lres.append(entier)
        if som>=n:
            return lres[::-1]
    return []
            
            
        
        
        
    
    
