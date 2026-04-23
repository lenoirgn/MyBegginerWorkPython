from typing import Callable
import sys

sys.path.append("/home/lenoirgn/Documents/ap_tdm_mamadou")

from tdm10.apqueue import *
from tdm10.apstack import *
from tdm09.aplst import *

def insertion(liste: list[any], i: int, comp: Callable[[any, any], int]):
    """
    insert l'élément `liste[i]` dans la tranche `liste[0:i]`.
    après exécution, `liste[0:i+1]` est triée.
    précondition : liste[0:i] est triée
    """
    while i>0 and comp(liste[i],liste[i-1])<0:
        liste[i],liste[i-1]=liste[i-1],liste[i]
        i-=1


def compare(a:any,b:any)->int:
    if a>b:
        return 1
    elif a<b:
        return -1
    else:
        return 0

def indice_dicho(liste: list[any], elt: int,a:int,b:int,comp:Callable[[any, any], int])->int:
    while a<b and comp(elt,liste[a])>0:
        a+=1
    return a

def tri_insert_dicho(liste: list[any], comp: Callable[[any, any], int] = compare):
    """
    trie la liste en utilisant l'insertion dichotomique.
    précondition : aucune
    exemples :
    $$$ l = []
    $$$ tri_insert_dicho(l)
    $$$ l
    []
    $$$ l = [3, 1, 4, 1, 5]
    $$$ tri_insert_dicho(l)
    $$$ l
    [1, 1, 3, 4, 5] """
    for i in range(1,len(liste)):
        indice=indice_dicho(liste,liste[i],i,len(liste),comp)
        insertion(liste,indice,comp)

l=[3, 1, 4, 1, 5]
tri_insert_dicho(l,compare)
#print(l)

def copie_file(qu: ApQueue) -> ApQueue:
    """
    Renvoie une copie de la file passée en paramètre.
    précondition : aucune
    $$$ qu = ApQueue()
    $$$ str(copie_file(qu))
    '→→'
    $$$ for el in (1, 2, 3): qu.enqueue(el)
    $$$ str(copie_file(qu))
    '→3|2|1→'
    $$$ str(qu)
    '→3|2|1→'
    """
    temp=ApQueue()
    copie=ApQueue()
    while not qu.is_empty():
        el=qu.dequeue()
        temp.enqueue(el)
        copie.enqueue(el)
    while not temp.is_empty():
        qu.enqueue(temp.dequeue())
    return copie

qu = ApQueue()
for i in range(1,7):
    qu.enqueue(i)

#print(qu)
#print(copie_file(qu))
#print(qu)
signes="-*+/"
def est_expression_valide (file:ApQueue)->bool:
    copie=copie_file(file)
    comp_nb=0
    comp_signe=0
    while not copie.is_empty():
        el=copie.dequeue()
        if str(el).isdigit():
            comp_nb+=1
        elif el in signes:
            comp_signe+=1
    return comp_nb==1+comp_signe

l=[2,3,"+",1,"-","+"]
file=ApQueue()
for el in l:
    file.enqueue(el)

#print(est_expression_valide(file))
#print(file)

def evalue_expression (chaine:str)->int:
    file=ApQueue()
    for car in chaine:
        file.enqueue(car)
    if est_expression_valide(file):
        pile=ApStack()
        res=0
        for el in chaine:
            if not str(el).isdigit():
                droite = pile.pop()
                gauche = pile.pop()
                if el=="+":
                    res=int(gauche)+int(droite)
                elif el=="-":
                    res=int(gauche)-int(droite)
                elif el=="*":
                    res=int(gauche)*int(droite)
                elif el=="/":
                    res=int(gauche)/int(droite)
                pile.push(res)
            else:
                pile.push(el)
            print(pile)
    return pile.pop()

#print(evalue_expression("234*+56*+"))


def concatenation(li1:ApLst,li2:ApLst)->ApLst:
    if li1.is_empty() :
        return li2
    else:
        return ApLst(li1.head(),concatenation(li1.tail(),li2))


Liste=ApLst(2, ApLst(5, ApLst(0, ApLst())))
Liste2=ApLst(5, ApLst(2, ApLst(6, ApLst())))

#print(concatenation(Liste,Liste2))
def plus_petit(li:ApLst,a:int):
    if li.is_empty() :
        return li

    if li.head()<a:
        return concatenation(ApLst(li.head(),ApLst()),plus_petit(li.tail(),a))
    else:
        return plus_petit(li.tail(),a)


def plus_grand(li:ApLst,a:int):
    if li.is_empty() :
        return li
    if li.head()>=a:
        return concatenation(ApLst(li.head(), ApLst()), plus_grand(li.tail(), a))
    else:
        return plus_grand(li.tail(), a)


def partition(li:ApLst,a:int)->(ApLst,ApLst):
    sup=plus_grand(li,a)
    inf=plus_petit(li,a)
    return sup,inf

#print(partition(Liste,3))

def tri_rapide(li:ApLst)->ApLst:
    if li.is_empty() :
        return ApLst()
    else:
        pivot=li.head()
        sup,inf=partition(li.tail(),pivot)
        sup_f=tri_rapide(sup)
        inf_f=tri_rapide(inf)
        return concatenation(inf_f,ApLst(pivot,sup_f))

l=tri_rapide(Liste)
print(l)

