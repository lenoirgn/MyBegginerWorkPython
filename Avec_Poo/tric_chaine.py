def tri_chaine(chaine:str)->str:
    return "".join(sorted(chaine))

def sont_anagrammes(chaine:str,chaine2:str)->bool:

    return tri_chaine(chaine) == tri_chaine(chaine2)

def select_car_min(chaine:str)->tuple[str,str,str]:
    c=tri_chaine(chaine)[0]
    i=chaine.index(c)
    return chaine[:i],c,chaine[i+1:]

#print(select_car_min("niche"))

def est_chaine_triee(chaine:str)->bool:
    s1,c,s2=select_car_min(chaine)
    for car in s1:
        if car >c:
            return False
    for car in s2:
        if car < c:
            return False
    return True

#print(est_chaine_triee("bca"))

def trie_chaine(chaine:str)->str:
    if len(chaine)<=1:
        return chaine

    s1,c,s2=select_car_min(chaine)
    return trie_chaine(s1)+c+trie_chaine(s2)

print(trie_chaine("djenaba"))


def trie_chainee(chaine: str) -> str:
    if len(chaine) <= 1:
        return chaine

    # select_car_min renvoie : min, avant, après
    s1, c, s2 = select_car_min(chaine)

    # on trie ce qu'il y a avant et après
    return trie_chainee(s1) + c + trie_chainee(s2)

#print(trie_chainee("djenaba"))
#Pockemons
def lire_pockemons(chaine:str)->list[dict]:
    with open(chaine,"r") as f:
        entete=f.readline().strip().split(';')
        liste=f.readlines()
    lres=[]
    for elt in liste:
        elt.strip()
        elt = elt.split(';')
        dico = {}
        for i in range(len(elt)):
          dico[entete[i]]=elt[i]
        lres.append(dico)
    return lres

base=lire_pockemons("pockemons.txt")



def comp_par_def(pock1:dict,pock2:dict)->int:
    if pock1["def"]>pock2["def"]:
        return 1
    elif pock1["def"]<pock2["def"]:
        return -1
    else:
        return 0

def recupere_values(dico:dict)->list[any]:
    liste = []
    for value in dico.values():
        liste.append(value)
    return liste


def ecrire_pockemons(fnom:str,base:list[dict]):
    entete=[]
    for key in base[0].keys():
        entete.append(key)
    grille=[]
    for pock in base:
        valeur=recupere_values(pock)

        grille.append(";".join(valeur))
    with open(fnom,"w") as f:
        f.write(";".join(entete)+'\n')
        for elt in grille:
            f.write(str(elt))
#ecrire_pockemons("new.txt",base)
def valeur (li:list,saut:tuple[int,int])->int:
    return li[saut[1]]-li[saut[0]]

def saut_max_exhaustif(li):
    maxi=valeur(li,(0,0))
    for i in range(len(li)):
        for j in range(i,len(li)):
            temp=valeur(li,(i,j))
            if temp>maxi:
                maxi=temp

    return maxi

l=[3,5,6,7,2,0,-1]
print(saut_max_exhaustif(l))
def saut_max_recursif(li):
    if len(li)==2:
        return max(valeur(li,(0,0)),valeur(li,(1,0)))
    else:
        l1=li[:len(li)//2]
        l2=li[len(li)//2:]






