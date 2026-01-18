def nb_ligne(grille:list[list[int]])->int:
    return len(grille)
def nb_colonne(grille:list[list[int]])->int:
    return len(grille[0])

def init_grille(fichier:str)->list[list[int]]:
    with open(fichier,'r') as f:
        nb_ligne=f.readline()
        nb_colonne=f.readline()
        liste_entier=f.readlines()

    ligne=[0]*nb_colonne
    grille=[]
    for i in range(nb_ligne):
        grille.append(ligne.copy())
    nouv_grille=deepcopy(grille)
    for elt in liste_entier:
        elt=elt.strip()
        elt=elt.split(' ')
        nouv_grille[int(elt[0])][int(elt[1])]+=int(elt[2])
    return nouv_grille

def poser_valeur(grille:list[list[int]],i:int,j:int,valeur:int)->list[list[int]]:
    nouv_grille=deepcopy(grille)
    nouv_grille[i][j]=valeur
    return nouv_grille

