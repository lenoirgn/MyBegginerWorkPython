from recherche import compare

def tri_max_indice(liste:list[any],comp:callable([int,int]))->int:
    imax=len(liste)-1
    for i in range(imax):
        if comp(liste[i],liste[imax])==1:
            imax=i
    return imax

def tri_sel_max(liste:list[any],comp:callable([int,int])):
    for i in range(len(liste)-1):
        imax=tri_max_indice(liste[:len(liste)-i],comp)
        j=len(liste)-1-i
        liste[j],liste[imax]=liste[imax],liste[j]

def insere(indice:int,liste:list[any],comp:callable([int,int])):
    while indice<len(liste)-1 and comp(liste[indice],liste[indice+1])==1:
        liste[indice],liste[indice+1]=liste[indice+1],liste[indice]
        indice+=1

def echange(liste:list[int],j:int,i:int):
    liste[i],liste[j]=liste[j],liste[i]

def glisser(li:list[int],a:int ,comp:callable([int,int])):
    while a<len(li)-1 and comp(li[a],li[a+1])==1:
        li[a],li[a+1]=li[a+1],li[a]
        a+=1

def tri(liste:list[int],comp:callable([int,int])):
    for i in range(len(liste)-2,-1,-1):
        glisser(liste,i,comp)

def renverser_sommet(liste:list[int], a:int):
    i = 0
    j = a - 1
    while i < j:
        echange(liste, i, j)
        i += 1
        j -= 1

def tri_crepes(liste:list[int],a:int,b:int,comp:callable([int,int])=compare):

    if b is None:
        b=len(liste)
    while a<b :
        imax=tri_max_indice(liste[a:b],comp)
        print(imax)
        renverser_sommet(liste,imax+1)
        print(liste)
        a+=1

liste=[4,2,13,36,9,10,2,13,1,15]
tri_crepes(liste,0,None)

print(liste)

