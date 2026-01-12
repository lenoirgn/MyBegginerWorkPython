def colonne(grille:list[list[str]],ind:int)->list[str]:
    """ Renvoie  la colonne d’indice ind

    Précondition : ind<len(ligne)
    Exemple(s) :
    $$$ colonne([['','','3',],['','','3',],['','','3',]],2)
    ['3','3','3']
    """
    colonne=[]
    for i in range(len(grille)):
        colonne.append(grille[i][ind])
    return colonne
def transpose(grille:list[list[str]])->list[list[str]]:
    """ Renvoie une nouvelle grille qui est la transposée du paramètre

    Précondition : 
    Exemple(s) :
    $$$ transpose([['1','2','3'],['4','5','6']])
    [['1','4'],['2','5'],['3','6']]
    """
    nouv_grille=[]
    for i in range(len(grille[0])):
        nouv_grille.append(colonne(grille,i))
    return nouv_grille
def verification_bas(nbligne:int,nbcol:int,i:int,j:int)->bool:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ verification_bas(2,3,1,2)
    False
    $$$ verification_bas(3,3,1,1)
    True
    $$$ verification_bas(3,3,1,2)
    False
    """
    return i+1 <nbligne and j+1<nbcol
def verification_haut(nbligne:int,nbcol:int,i:int,j:int)->bool:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ verification_haut(2,3,0,2)
    False
    $$$ verification_haut(3,3,1,3)
    True
    $$$ verification_haut(3,3,1,0)
    False
    """
    return i-1>=0 and j-1>=0
def cases_premiere_diagon(nbligne:int,nbcol:int,i:int,j:int)->list[tuple[int,int]]:
    """ Renvoie les indices de la diagonale passant par i,j.

    Précondition : 
    Exemple(s) :
    $$$ cases_premiere_diagon(3,3,1,1)
    [(0,0),(1,1),(2,2)]
    $$$ cases_premiere_diagon(5,7,4,4)
    [(0,0),(1,1),(2,2),(3,3),(4,4)]
    $$$ cases_premiere_diagon(5,7,6,4)
    [(2,0),(3,1),(4,2),(5,3),(6,4)]
    """
    liste0=[]
    liste1=[]
    h0=i-1
    h1=j-1
    b0=i+1
    b1=j+1
    
    while (h0>=0 and h1>=0) or (b0<nbligne and b1 <nbcol):
        if verification_bas(nbligne,nbcol,i,j):
            liste1.append((b0,b1))
            b0+=1
            b1+=1
        if verification_haut(nbligne,nbcol,i,j):
            liste0.append((h0,h1))
            h0-=1
            h1-=1
    lres=liste0[::-1]+[(i,j)]+liste1
    return lres
    
   
    
    
    