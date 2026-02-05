def somme(a:int, b:int) -> int:
    if b == 0:
        return a
    else:
        return somme(a+1,b-1)

def produit(a:int, b:int) -> int:
    if a == 0:
        return 0
    else:
        return b +produit(a-1,b)

def puissance(a:int, n:int) -> int:
    if a == 0 and n == 0:
        return 0
    elif n == 0:
        return 1
    else:
        return a * puissance(a,n-1)

# uniquement a=2

def puissance_deux(a:int, n:int) -> int:
    if n == 0:
        return 1
    elif n%2== 0:
        temp=puissance_deux(a,n//2)*puissance_deux(a,n//2)
        return temp
    else:
        return 2*puissance_deux(a,n-1)


def nbre_chiffres(a:int) -> int:
    if a <= 9:
        return 1
    else:
        return 1+nbre_chiffres(a//10)

def somme_chiffres(a:int) -> int:
    if a <=9:
        return a
    else:
        return a%10+somme_chiffres(a//10)
from math import gcd
def est_divible_par_trois(a:int)->bool:
    # if a == 0:
    #     return True
    # else:
    #     return gcd(3,somme_chiffres(a))==3
    if a <10:
        return a in (0,3,6,9)
    else:
        return est_divible_par_trois(somme_chiffres(a))


def euclide(a:int,b:int)->int:
    assert b!=0,"b ne doit pas etre nul"
    if a%b == 0:
        return b
    else:
        return euclide(b,a%b)

def nb_occurences(mot:str,car:str)->int:
    if mot=='':
        return 0
    elif car==mot[0]:
        return 1+nb_occurences(mot[1:],car)
    else:
        return nb_occurences(mot[1:],car)

def indice(mot: str, car: str) -> int:
    if len(mot) == 0:
        raise ValueError("char not found")
    elif mot[0] == car:
        return 0
    else:
        return 1 + indice(mot[1:], car)

def liste_somme_rec(liste:list[int])->int:
    if len(liste) == 1:
        return liste[0]
    return liste[0]+liste_somme_rec(liste[1:])

def liste_produit_rec(liste:list[int])->int:
    if len(liste) == 1:
        return liste[0]
    return liste[0]*liste_produit_rec(liste[1:])

def split(liste: list[int])->tuple[list[int],list[list[int]]]:
    if len(liste) == 0:
        return ([],[])
    elif len(liste)%2 == 0:
        tuple([].append(liste[0]))

        return split(liste[1:])
    else:
        tuple([], [].append(liste[0]))
        return split(liste[1:])




