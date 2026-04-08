import sys


sys.path.append("/home/lenoirgn/Documents/ap_tdm_mamadou")

from tdm10.apstack import *
from random import randint
p1=ApStack()
p2=ApStack()

[p1.push(i) for i in range(25,0,-3)]
[p2.push(i) for i in range(50,5,-5)]


def chaine (pile: ApStack):
    temp=ApStack()
    res=''
    while not pile.is_empty():
        temp.push(pile.top())
        res=res+str(pile.pop())+'\n'
    while not temp.is_empty():
        pile.push(temp.pop())
    return res

def repre(pile:ApStack):
    if pile.is_empty():
        return '['
    else:
        top=pile.pop()
        res=repre(pile)+' '+str(top)
        pile.push(top)
        return res

def merge(p1:ApStack,p2:ApStack):
    l=[]
    while not p1.is_empty() and not p2.is_empty():

        if p1.top()<p2.top():
            l.append(p1.pop())
        else:
            l.append(p2.pop())
    while not  p1.is_empty() :
        l.append(p1.pop())
    while not p2.is_empty() :
        l.append(p2.pop())
    return l
def to_bin(entier:int):
    res=ApStack()
    while entier!=0:
        res.push(entier%2)
        entier//=2
    return res


def parenthese(chaine: str):
    pile = ApStack()
    for c in chaine:
        if c == '(':
            pile.push(c)
        elif c == ')':
             if pile.is_empty():
                return False
             pile.pop()

    return pile.is_empty()
