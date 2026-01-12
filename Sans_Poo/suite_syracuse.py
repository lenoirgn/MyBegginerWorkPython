# suite syracuse voir : https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse
def est_pair(entier:int)->bool:
    """ Renvoie True si l'entier est pair

    Précondition : 
    Exemple(s) :
    $$$ est_pair(4)
    True
    $$$ est_pair(3)
    False
    """
    return entier%2==0
    
def  suite_syracuse(entier:int)->list[int]:
    """Renvoie la liste des termes de la suite de Syracuse jusqu’au premier 1 rencontré inclu

    Précondition :entier>0 
    Exemple(s) :
    $$$ suite_syracuse(14)
    [14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    $$$ suite_syracuse(10)
    [10, 5, 16, 8, 4, 2, 1]
    $$$ suite_syracuse(2)
    [2, 1]
    """
    
    lres=[entier]
    
    while entier!=1:
        if est_pair(entier):
            entier=entier/2
        else:
            entier=(entier*3)+1
        lres.append(entier)
    return  lres