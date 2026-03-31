import sys

from pygments.lexers.apl import APLLexer

sys.path.append("/home/lenoirgn/Documents/ap_tdm_mamadou")

from tdm09.aplst import *

Liste=ApLst(3, ApLst(1, ApLst(4, ApLst())))
Liste2=ApLst(5, ApLst(2, ApLst(6, ApLst())))
liste3=ApLst(Liste,Liste2)

def length(liste: ApLst):
    tem=liste
    i=0
    while not tem.is_empty():
        i+=1
        tem=tem.tail()
    return i

#print(length(ApLst(3, ApLst(1, ApLst(4, ApLst())))))
#>> 3
def length_rec(liste: ApLst,i:int):
    if liste.is_empty():
        return i
    else:
        return length_rec(liste.tail(),i+1)

#print(length_rec(Liste,0))
#>> 3

def length_rec_v2(liste: ApLst):
    "Return the length of the list"
    if liste.is_empty():
        return 0
    else:
        return  1 +length_rec_v2(liste.tail())

def nth(liste:ApLst,indice:int):
    "Return the nth element in a list"

    if indice==0:
        return liste.head()
    else:
        return nth(liste.tail(),indice-1)

def last(liste:ApLst):
    "Return the last element in a list"
    if liste.is_empty():
        raise Exception("Liste est vide")
    elif length(liste)==1:
        return liste.head()
    else:
        return last(liste.tail())
def concat(li1:ApLst,li2:ApLst):
    "Concatenate two lists"
    if li1.is_empty() :
        return li2
    else:
        return ApLst(li1.head(),concat(li1.tail(),li2))


def reverse(liste:ApLst):
    "Reverse a list"

    if length(liste)==1:
        return liste
    else:
        return concat(reverse(liste.tail()),ApLst(liste.head(),ApLst()))



def flatten(liste:ApLst):
    "Flatten a list"
    


print(length(liste3))
print(flatten(liste3))

