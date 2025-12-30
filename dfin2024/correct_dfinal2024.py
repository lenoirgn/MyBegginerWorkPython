def charger_grille(ficher:str):
    """Renvoie la grille"""
    with open(ficher, "r") as fichier:
        nb_ligne=int(fichier.readline())
        nb_colonne=int(fichier.readline())
        grille=[]
        for i in range(nb_ligne):
            ligne=[]
            for j in range(nb_colonne):
                case=fichier.readline()
                case=case.split(",")
                ligne.append(((case[0]),(case[1])))
            grille.append(ligne)
    return grille

charger_grille("grille.txt")
def est_permutation(liste:list[int])->bool:
    """ 
    
    Précondition : 
    Exemple(s) :
    $$$ est_permutation([2, 1, 3, 4])
    True
    $$$ est_permutation([2,3, 4,1])
    True
    $$$ est_permutation(([2, 1, 3,5]))
    False
    $$$ est_permutation(([1, 1, 3,4]))
    False
    """
    
    for i in range(1,len(liste)+1):
        if not i in liste:
            return False
    return True
        
SEPH_DIFF = '|' # séparateur horizontal entre 2 valeurs de zones différentes
SEPH = '  ' # séparateur horizontal entre 2 valeurs de zones identiques
SEPV_DIFF = '---' # séparateur vertical entre 2 zones différentes
SEPV = ' ' # séparateur vertical entre 2 zones identiques
COIN = '+' # coin d'une case
ESP = ' ' # espacement de part et d'autre d'une valeur
def case_formatee(couple:tuple[int, int])->str:
    """ 
    Précondition : 
    Exemple(s) :
    $$$ case_formatee((0,1))
    ESP + '0' + ESP
    """
    return ESP + str(couple[0]) + ESP
def ligne_formatee(liste:list[tuple[int,int]])->str:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) : 
    $$$ ligne_formatee([(0, 1), (2, 1), (3, 2)])
    "| 0  2 | 3 |"
    $$$ ligne_formatee([(0, 1), (2, 1), (3, 2), (6, 3),(3,1)])
    "| 0  2  3 | 3 | 6 |"
    """
    res=SEPH_DIFF
    list_temp=[]
    for i in range(len(liste)):
        if not liste[i][1] in list_temp:
            list_temp.append(liste[i][1])
    for elt0 in list_temp:
        for elt in liste:
            if elt0==elt[1]:
                res+=case_formatee(elt)
        res+=SEPH_DIFF
    return res
def separation_ligne (liste1:list[tuple[int, int]],liste2:list[tuple[int, int]])->str:
    """
    Précondition : 
    Exemple(s) :
    $$$ separation_ligne([(0, 1), (2, 2), (3, 3)], [(0, 2), (2, 2), (3, 4)])
    "+---+ +---+"
    $$$ separation_ligne([(0, 1), (2, 2), (3, 3)], [(1, 1), (2, 2), (0, 3)])
    "+  + +  +"
    """
    for i in range(len(liste1)):
        if liste1[i][1] !=liste2[i][1]:
            return COIN+SEPV_DIFF+COIN+' '+COIN+SEPV_DIFF+COIN 
    return COIN+SEPH+COIN+' '+COIN+SEPH+COIN 
        
liste1 = ['d', '#', 'y', 'r', 'z', 'g']
liste2 = ['d', '9', '@', 'y', 'z']
liste3 = ['#', 'r', 'g']
liste0=['#', 'g', 'r']
def position_caractere(carac:str,liste:list[str])->int:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ position_caractere('g', liste1)
    5
    $$$ position_caractere('h', liste1)
    6
    """
    res=''
    i=0
    while i<len(liste) and liste[i]!=carac:
        i+=1
    return i
def au_moins_n_motifs(entier:int,liste:[str],motif:[str])->bool:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ au_moins_n_motifs(2, ['a', 'b', 'c', 'a', 'b', 'b', 'a'], ['a', 'b'])
    True
    $$$ au_moins_n_motifs(2, ['a', 'a', 'a'], ['a', 'a'])
    True
    au_moins_n_motifs(3, ['a', 'b', 'c', 'a', 'b', 'b', 'a', 'c', 'b'], ['a', 'b'])
    False
    """
    compt=0
    dep=0
    fin=len(motif)
    while fin<=len(liste) and entier>compt:
        if liste[dep:fin]==motif:
            compt+=1
        dep+=1
        fin+=1
    return entier==compt
from random import choice   
def genere_liste_sans_begaiement(entier:int,liste:[str])->list[str]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    
    res=[]
    prec=''
    while len(res)<entier:
        elemt=choice(''.join(liste))
       
        while elemt==prec:
             elemt=choice(''.join(liste))
        res.append(elemt)
        prec=elemt
    return res      
         
def affiche_sans_begaiement(liste:list[str]):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    print(genere_liste_sans_begaiement(5,liste))
    
def est_cache_dans(liste:list[str],liste1:list[str])->bool:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ est_cache_dans(liste3, liste1)
    True
    $$$ est_cache_dans(liste0, liste1)
    False
    $$$ est_cache_dans(['a', 'b', 'c', 'e','7', 'q', 'l'],['c', 'q', 'm'] )
    False
    """   
    for i in range(len(liste)-1):
        if position_caractere(liste[i],liste1)>position_caractere(liste[i+1],liste1):
            return False
    return True
        
        
                             
        
    
    
    
    
    
    