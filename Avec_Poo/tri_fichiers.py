import sys
from functools import cmp_to_key

from uaclient.entitlements.entitlement_status import ApplicationStatus

sys.path.append("/home/lenoirgn/Documents/ap_tdm_mamadou")
from tdm09.aplst import *
from tdm10.apstack import *

Liste=ApLst(6, ApLst(3, ApLst(4, ApLst())))
Liste2=ApLst(2, ApLst(5, ApLst(6, ApLst())))
li=ApLst()

def tri_par_nom(liste:list[str])->list[str]:
    return (sorted(liste)[::-1])
   # lres=[]
   # mini=liste[0]
   # for i in range(1,len(liste)):
   #      if liste[i]<mini:
   #          lres.append(liste[i])
   #      else:
   #          lres.append(mini)
   #          mini=liste[i]
   # lres.append(mini)
   # return lres[::-1]

def nombre_cars(fnom:str)->int:
    with open(fnom,'r') as f:
        liste=f.readlines()
    res=0
    for elt in liste:
        elt=elt.strip()
        res+=len(elt)
    return res

def cmp_par_taille(s1:str,s2:str)->int:
    len_s1=nombre_cars(s1)
    len_s2=nombre_cars(s2)
    if len_s1>len_s2 or s1>s2:
        return 1
    elif len_s1<len_s2 or s2>s1:
        return -1
    else:
        return 0

def  tri_par_nb_cars(li:list[str])->list[str]:

    return sorted(li,key=cmp_to_key(cmp_par_taille))


def sauvegarder_infos(li:list[str]):
    with open("ls_lr.csv","w") as f:
        for elt in li:
            n=nombre_cars(elt)
            f.write(elt+";"+str(n)+"\n")


def zero_ou_un_element(li:ApLst)->bool:
    if li.is_empty() or li.tail().is_empty():
        return True
    else:
        return False

def decoupage(li: ApLst) -> tuple[ApLst, ApLst]:
    if li.is_empty():
        return ApLst(), ApLst()

    elif zero_ou_un_element(li):
        return ApLst(li.head(), ApLst()), ApLst()

    else:
        left, right = decoupage(li.tail().tail())
        left = ApLst(li.head(), left)
        right = ApLst(li.tail().head(), right)
        return left, right


print(decoupage(Liste))

def fusion (li1: ApLst,li2:ApLst)->ApLst:
    if li1.is_empty():
        return li2
    elif li2.is_empty():
        return li1
    else:
        if li1.head()>li2.head():
            return ApLst(li2.head(),fusion(li1,li2.tail()))
        else:
            return ApLst(li1.head(),fusion(li1.tail(),li2))

#print(fusion(Liste,Liste2))

def tri_fusion (li:ApLst):
    if  zero_ou_un_element(li):
        return li
    else:
        left, right = decoupage(li)
        tri_left = tri_fusion(left)
        tri_right = tri_fusion(right)
        return fusion(tri_left,tri_right)


def extrait_min(pile:ApStack):
    temp=ApStack()
    mini = pile.pop()
    temp.push(mini)
    trouve = True
    while not pile.is_empty():
        elt=pile.pop()
        temp.push(elt)
        if elt<mini:
            mini=elt
    while not temp.is_empty():
        elt=temp.pop()
        if elt == mini and trouve:
            trouve= False
        else:
            pile.push(elt)
    return mini

pile=ApStack()
pile.push(5)
pile.push(1)
pile.push(2)
pile.push(9)
pile.push(1)
def tri_par_selection(pile:ApStack):
    temp=ApStack()
    while not pile.is_empty():
        mini=extrait_min(pile)
        temp.push(mini)
    while not temp.is_empty():
        pile.push(temp.pop())


tri_par_selection(pile)
#print(pile)
