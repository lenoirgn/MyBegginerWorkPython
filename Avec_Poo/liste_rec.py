import sys

from pygments.lexers.apl import APLLexer

sys.path.append("/home/lenoirgn/Documents/ap_tdm_mamadou")

from tdm09.aplst import *

Liste=ApLst(3, ApLst(1, ApLst(4, ApLst())))
Liste2=ApLst(5, ApLst(2, ApLst(6, ApLst())))
liste4=ApLst()
liste3=ApLst(Liste,ApLst(liste4,ApLst(Liste2,ApLst())))

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
    lres=ApLst()
    for i in range(length(liste)):
        print(lres)
        lres=concat(lres,nth(liste,i))
    return lres

def zip(li1:ApLst,li2:ApLst):
    "Zip  liste1 and liste2"
    li1=reverse(li1)
    li2=reverse(li2)
    lres=ApLst()
    for i in range(length(li1)):
        lres=ApLst((li1.head(),li2.head()),lres)
        li1=li1.tail()
        li2=li2.tail()
    return lres
def unzip(liste:ApLst):
    "Unzip a liste"
    li1=ApLst()
    li2=ApLst()
    for i in range(length(liste)):
        li1=ApLst(liste.head()[0],li1)
        li2=ApLst(liste.head()[1],li2)
        liste=liste.tail()
    return reverse(li1),reverse(li2)





