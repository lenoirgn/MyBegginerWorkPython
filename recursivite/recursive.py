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

# dans  a^n on a n-1 produit pour n >1
# nb_produit=(n-1)

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
    if a == 0:
        return True
    else:
        return gcd(3,somme_chiffres(a))==3

def euclide(a:int,b:int)->int:
    assert b!=0,"b ne doit pas etre nul"
    if a%b == 0:
        return b
    else:
        return euclide(b,a%b)

def nb_occurences(mot:str,car:str)->int:
    compt=0
    for carac in mot:
        if carac==car:
            compt+=1
    return compt

def indice(mot:str,car:str)->int:
   