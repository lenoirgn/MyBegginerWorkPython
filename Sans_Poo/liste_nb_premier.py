def  est_premier(entier:int)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ est_premier(9)
    False
    $$$ est_premier(7)
    True 
    """
    if entier<2:
        return False
    i=2
    while i<entier and entier%i!=0:
        i+=1
    return i>=entier

def liste_nb_premier(entier:int)->list:
    """ Renvoie la liste de nombre premier
    Précondition : entier>2
    Exemple(s) :
    $$$ liste_nb_premier(2)
    [2]
    $$$ liste_nb_premier(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    
    """
    lres=[]
    for i in range(entier+1):
        if est_premier(i):
            lres.append(i)
    return lres
    
    