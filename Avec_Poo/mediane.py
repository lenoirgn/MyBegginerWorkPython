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
    if len(li)==0:
        return []
    elif len(li)==1:
        return li
    else:
        l_inf, l_sup = inf_sup(li, li[0])
        l_inf.append(li[0])
        inf=tri_rapide(l_inf)
        sup=tri_rapide(l_sup)
        return inf+sup

def sel_rapide(li: list[int|float], k: int) -> int|float:
    l_inf, l_sup = inf_sup(li, li[k])
    if len(l_inf)== k :
        return li[k]



liste=[10,2,33,5,60,7,9,1,11,12,14]
print(tri_rapide(liste))