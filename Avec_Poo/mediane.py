import sys

sys.path.append("/home/lenoirgn/Documents/ap_tdm_mamadou")

from tdm10.apstack import *

def inf_sup(li: list[int|float], x: int|float) -> tuple[list[int|float], list[int|float]]:
    l_inf=[]
    l_sup=[]
    for elem in li:
        if elem > x:
            l_sup.append(elem)
        elif elem < x:
            l_inf.append(elem)
    return l_inf, l_sup

def mediane1(li: list[int|float]) -> int|float:
    for elem in li:
        l_inf, l_sup = inf_sup(li, elem)
        if len(l_inf) <= len(li)//2  and len(l_sup) <= len(li)//2:
            return elem


#len(l_inf)=i
#len(l_sup)=n-i-1
# n//2+1-n<= i <=n//2
def tri_rapide(li: list[int|float]) -> list[int| float]:
    if len(li)<=1:
        return li
    else:
        l_inf, l_sup = inf_sup(li, li[0])
        inf=tri_rapide(l_inf)
        sup=tri_rapide(l_sup)
        return inf+[li[0]]+sup

def sel_rapide(li: list[int|float], k: int) -> int|float:
    pivot=li[0]
    l_inf, l_sup = inf_sup(li, pivot)
    if len(l_inf)== k :
        return pivot
    elif len(l_inf)> k:
        return sel_rapide(l_inf,k)
    elif len(l_inf)< k:
        new_k=k-len(l_inf)-1
        return sel_rapide(l_sup,new_k)





liste=[10,2,33,5,60,7,9,1,11,12,14]
print(tri_rapide(liste))

#Jeu
def initialisation(n: int) -> dict[str, ApStack]:
    pile=ApStack()
    for n in range(n,0,-1):
        pile.push(n)
    dico={"A":pile,"B":ApStack(),"C":ApStack()}
    return dico

def deplace(plateau: dict[str, ApStack], depart: str, arrivee: str) -> None:
    pile_depart=plateau[depart]
    pile_arrivee=plateau[arrivee]
    pile_arrivee.push(pile_depart.pop())

def tour_intermediaire(A:str, B:str) -> str:
   keys=dic.keys()
   for key in keys:
       if A!=key and B!=key:
           return key
   raise ValueError(" Erreur de value")

def solution(depart: str, arrivee: str, n: int) -> list[tuple[str, str]]:
    lres = []
    pile = ApStack()

    # On pousse le quadruplet initial
    pile.push((depart, arrivee, n, True))

    while not pile.isEmpty():
        a, b, m, debut = pile.pop()

        # Tour intermédiaire
        c = tour_intermediaire(a, b)

        if m > 0:
            if debut:
                # On repousse le même quadruplet mais avec debut = False
                pile.push((a, b, m, False))

                # On doit d'abord traiter le sous-problème : déplacer m-1 disques de a vers c
                pile.push((a, c, m - 1, True))

            else:
                # Mouvement réel d’un disque : a → b
                lres.append((a, b))

                # Ensuite on déplace m-1 disques de c vers b
                pile.push((c, b, m - 1, True))

    return lres





dic=initialisation(5)
p1=ApStack()
p2=ApStack()
[p1.push(i) for i in range(0,5)]
[p2.push(i) for i in range(5,10)]
dic["B"]=p1
dic["C"]=p2
print(dic)
deplace(dic,"B","C")
print(dic)



