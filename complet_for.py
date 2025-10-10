#complementaire for
def compte_posits(lentier:list[int])->int:
    """ renvoie le nombre d'entier positif
    Précondition : 
    Exemple(s) :
    $$$ compte_posits([])
    0
    $$$ compte_posits([-4,5,8])
    2
    """
    nb_occu=0
    for elt in lentier:
        if elt >=0:
            nb_occu+=1
    return nb_occu

from statistics import mean 
def variances(lentier:list[int])->float:
    """ renvoie la variance des éléments de la liste
    Précondition : 
    Exemple(s) :
    $$$ variances([7,8,4,5])
    2.5
    $$$ variances([5,5])
    0
    """
    variance=0.0
    moyenne=mean(lentier)
    for elt in lentier:
        
        variance+=1/len(lentier) *((elt - moyenne)**2)
       
    return variance
def incremente(lentier:list[int])->list[int]:
    """ Renvoie une liste incrementer

    Précondition :
    Exemple(s) :
    $$$ incremente([0, 3, -6, 12, -7])
    [1, 4, -5, 13, -6]
    """
    
    lres=[]
    for entier in lentier:
        lres.append(entier+1)
    return lres
def saisie(nb_fois:int)->str:
    """ 

    Précondition :
    Exemple(s) :
    $$$ 
    """
    reschaine=''
    for i in range(3):
       chaine=input("entrer un ou plusieurs caracteres : ")
       reschaine+=chaine
    return reschaine
def compte_point(chaine:str)->int:
    """ 

    Précondition :
    Exemple(s) :
    $$$ compte_point('Salut !! ca va ? oui...')
    6
    """
    somme=0
    list_point=['.',',',';','?','!']
    for carac in chaine:
       if carac in list_point:
          somme+=1
    return somme
def compte_point_list(chaine:list[str])->int:
    """ 

    Précondition :
    Exemple(s) :
    $$$ compte_point_list(['Salut !!', 'Tom,' 'ca va ?', 'tu as dit quoi ?!?!'])
    8
    """
    sommes=0
    for ele in chaine:
       sommes+=compte_point(ele)
    return sommes

def puissance(entier:int,exposant:int)->int:
    """ Renvoie la puissance

    Précondition :
    Exemple(s) :
    $$$ puissance(3, 0)
    1
    $$$ puissance(4, 1)
    4
    $$$ puissance(1, 5)
    1
    """
    return entier**exposant

def cumul_intervale(inf:int,sup:int)->list[int]:
    """

    Précondition :
    Exemple(s) :
    $$$ cumul_intervale(2, 4)
    [2, 6, 24]
    """
    lres=[]
    produit=1
    for i in range(inf,sup+1):
        produit*=i
        lres.append(produit)
    return lres

