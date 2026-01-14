# Partie Analyse et Traitement

def dimension_egale(grille0:list[list[int]],grille1:list[list[int]]) -> bool:
    "Verifie si les deux matrices ont les meme dimension"
    return len(grille0)==len(grille1) and len(grille0[0])==len(grille1[0])



def somme(grille0:list[list[int]],grille1:list[list[int]],choix:int)->list[list[int]] :
     "Fait la somme de deux matrices"
     result=[]
     for i in range (len(grille0)):
        ligne=[]
        for j in range (len(grille0[i])):
            if choix==1:
                res=grille0[i][j]+grille1[i][j]
            if choix==2:
                res=grille0[i][j]-grille1[i][j]
            ligne.append(res)
        result.append(ligne)
     return result


def sont_egale(grille:list[list[int]],grille1:list[list[int]]) -> bool :
    return len(grille[0])==len(grille1)


def Colonne(grille: list[list[int]], ind: int) -> list[int]:
    """ Renvoie  la colonne d’indice ind
    Précondition : ind<len(ligne)
    """
    colonne = []
    for i in range(len(grille)):
        colonne.append(grille[i][ind])
    return colonne


def transpose(grille: list[list[int]]) -> list[list[int]]:
    """ Renvoie une nouvelle grille qui est la transposée du paramètre
    """
    nouv_grille = []
    for i in range(len(grille[0])):
        nouv_grille.append(Colonne(grille, i))
    return nouv_grille
def somme_produit(liste: list[int],liste1: list[int])->int:
    somme=0
    for i in range(len(liste)):
        somme+=liste[i]*liste1[i]
    return somme


def produit(grille: list[list[int]], grille1: list[list[int]]) -> list[list[int]]:
    result = []
    transpose_grille1 = transpose(grille1)
    for i in range(len(grille)):
        ligne=[]
        for j in range(len(transpose_grille1)):
            somme=somme_produit(grille[i],transpose_grille1[j])
            ligne.append(somme)
        result.append(ligne)
    return result


def saisie(choix:int):
    liste=[]
    nb_ligne=int(input('Entrez le nombre de ligne: '))
    while nb_ligne < 0:
        print("Saisie invalide")
        nb_ligne = int(input('Entrez le nombre de ligne: '))
    liste.append(nb_ligne)
    if choix==1:
        liste.append(nb_ligne)
    else:
        nb_colonne=int(input('Entrez le nombre de colonne: '))
        while nb_colonne < 0:
            print("Saisie invalide")
            nb_ligne = int(input('Entrez le nombre de colonne: '))
        liste.append(nb_colonne)
    return liste

def grille_init(nb_ligne:int,nb_colonne:int)->list[list[int]]:
    matrice=[]
    for i in range(nb_ligne):
        liste=[]
        for j in range(nb_colonne):
            valeur=int(input(f'Entrez la colonne {j+1} de la Ligne {i+1}: '))
            liste.append(valeur)
        matrice.append(liste)
    return matrice



def main():
    liste=[]
    for i in range(2):
        print('Choix de type de matrice')
        print('1-Carre ')
        print("2- Rectangle")
        choix=int(input("Entrez le nombre de choix: "))
        while choix not in [1,2]:
            print("Saisie invalide")
            choix = int(input("Entrez le nombre de choix: "))
        liste_dimension=saisie(choix)
        grille=grille_init(liste_dimension[0],liste_dimension[1])
        liste.append(grille)
    print(f"Matrice1: {liste[0]}\t Matrice2: {liste[1]}")

    print("=== Menu d'opérations sur matrices ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Produit")
    choix =int( input("Entrez votre choix (1/2/3) : "))
    while choix not in [1,2,3]:
        print("Saisie invalide")
        choix = int(input("Entrez votre choix (1/2/3) : "))
    if choix==1:
        if dimension_egale(liste[0],liste[1]):
            result=somme(liste[0],liste[1],choix)
        else:
            return "Les matrices n'ont pas les meme dimensions "
    elif choix==2:
        if dimension_egale(liste[0],liste[1]):
            result=somme(liste[0],liste[1],choix)
        else:
            return "Les matrices n'ont pas les meme dimensions "
    else:
        if sont_egale(liste[0],liste[1]):
            result=produit(liste[0],liste[1])
        else:
            return "Les matrices ne remplissent pas les conditions pour le produit "
    return f"le resultat de l'operation est {result}"

if __name__=='__main__':
    print(main())

