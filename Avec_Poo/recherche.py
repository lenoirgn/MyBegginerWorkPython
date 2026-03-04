from compare import compare
from typing import Callable


def recherche(liste: list[int], a:int, b:int,elet: int) -> bool:
    for i in range(a,b):
        if liste[i]==elet:
            return True
    return False


def compare(a: int, b: int) -> int:
    if a>b:
        return 1
    elif a<b:
        return -1
    else:
        return 0

def indice(elet: int, liste: list[int], a: int=0, b: int=None, comp: Callable[[int, int], int] = compare) -> int:
    if b is None:
        b=len(liste)-1
    while a < b and comp(elet, liste[a])!=0:
        a += 1
    if liste[a]==elet:
        return a
    else:
        return -1

def indicev2(elet: int, liste: list[int], a: int=0, b: int=None, comp: Callable[[int, int], int] = compare) -> int:
    if b is None:
        b=len(liste)-1
    trouve=False
    while a < b and not  trouve:
        if liste[a]==elet:
            trouve=True
        else:
            a=a+1
    if trouve:
        return a
    else:
        return -1



def recherche_dicho_rec(elet: int,liste:list[int],a:int=0,b:int=None,comp: Callable[[int, int], int] = compare) -> int:
    if b is None:
        b=len(liste)-1
    d=a
    f=b-1
    if d<f:
        m=(d+f)//2
        if comp(elet,liste[m])>0:
            res= recherche_dicho_rec(elet,liste,m+1,f+1,comp)
        else:
            res= recherche_dicho_rec(elet,liste,d,m+1,comp)
    else:
        res= (a<b) and comp(elet,liste[d])==0
    return res

def recherche_dicho_indice(elem: int,liste:list[int],comp: Callable[[int, int], int] = compare) -> tuple[int,bool]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ recherche_dicho_indice(8,[2,3,5,6,7,9,12,19],compare)
    (False,5)
    """
    
    debut = 0
    fin = len(liste) - 1
    trouve = False
    indice = 0

    while debut <= fin and not trouve:
        milieu = (debut + fin) // 2
        if comp(liste[milieu], elem) == 0:
            trouve = True
            indice = milieu
        elif comp(liste[milieu], elem) == 1:
            fin = milieu - 1
        else:
            debut = milieu + 1

    if not trouve:
        indice = debut  # position d’insertion

    return (trouve, indice)


def recherche_dicho_rec_indice(elem: int,
                        liste: list[int],
                        a: int = 0,
                        b: int = None,
                        comp=compare) -> int:

    if b is None:
        b = len(liste) - 1

    # Intervalle vide → élément non trouvé
    if a > b:
        return -1

    m = (a + b) // 2

    if comp(liste[m], elem) == 0:         # trouvé
        return m
    elif comp(liste[m], elem) > 0:        # aller à gauche
        return recherche_dicho_rec_indice(elem, liste, a, m - 1, comp)
    else:                                 # aller à droite
        return recherche_dicho_rec_indice(elem, liste, m + 1, b, comp)

