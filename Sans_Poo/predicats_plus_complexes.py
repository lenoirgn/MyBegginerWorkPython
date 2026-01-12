# Compléter ici (noms, groupe, contenu fichier, date)
#Mamadou Radjaye sow,MI23, Traite_Predicat_complexe,21/09/2025
#
#
#
# Ne pas supprimer cette ligne. <trace>predicats_plus_complexes.py</trace>

####################
# Prédicats plus complexes
####################

def est_en_ete(jour:int, mois:int):
    """ Renvoie si on est en ete

    Précondition :mois>5 et mois<10
    Exemple(s) :
    $$$ est_en_ete(2,2)
    False
    $$$ est_en_ete(2,6)
    False
    $$$ est_en_ete(21,6)
    True
    $$$ est_en_ete(21,9)
    True
    $$$ est_en_ete(25,9)
    False
    $$$ est_en_ete(21,10)
    False
    """
    return (mois>=6 and jour>=21) and (mois>=6) and (mois<=9 and jour<=21)  


### Nombre mystere

def est_comprise(nombre:int)->bool:
    """ Renvoie si le nombre est comprise
    Précondition : 
    Exemple(s) :
    $$$ est_comprise(380)
    False
    $$$ est_comprise(425)
    True
    $$$ est_comprise(448)
    True
    """
    return nombre>410 and nombre<450
def est_double(nombre:int)->bool:
    """ Renvoie si le nombre est double de l'unite

    Précondition : 
    Exemple(s) :
    $$$ est_double(236)
    True
    $$$ est_double(145)
    False
    $$$ est_double(48)
    True
    """
    dizaine=nombre%100
    return nombre%10 == 2*(dizaine//10) 
    
def est_nombre_mystere(nombre:int)->bool:
    """ Renvoie True si ce le nombre mystere

    Précondition : nombre>410 et nombre<450
    Exemple(s) :
    $$$ est_nombre_mystere(380)
    False
    $$$ est_nombre_mystere(425)
    False
    $$$ est_nombre_mystere(448)
    True
    """
    return est_comprise(nombre) and est_double(nombre) and (nombre//100 + nombre%100+nombre%10)%2==0

### Intervalles

def ont_intersection_vide(deb1:int, fin1:int, deb2:int, fin2:int)-> bool:
    """ Renvoie si l'intersection est vide 

    Précondition :
    Exemple(s) :
    $$$ ont_intersection_vide(2,4,3,9)
    False
    $$$ ont_intersection_vide(2,3,4,9)
    True
    """
    return fin1<deb2


def intervalle1_contient_intervalle2(deb1:int, fin1:int, deb2:int, fin2:int)->bool:
    """ Renvoie si l'un contient l'autre

    Précondition :
    Exemple(s) :
    $$$ intervalle1_contient_intervalle2(2,4,3,9)
    False
    $$$ intervalle1_contient_intervalle2(2,4,7,9)
    False
    $$$ intervalle1_contient_intervalle2(2,9,3,6)
    True
    """
    return deb1<deb2 and fin1>fin2


# Décommenter et compléter la signature donnée puis faire la suite
def sont_intervalles_recouvrants(deb1:int, fin1:int, deb2:int, fin2:int)->bool:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ sont_intervalles_recouvrants(2,9,3,6)
    True
    $$$ sont_intervalles_recouvrants(2,4,3,6)
    True
    $$$ sont_intervalles_recouvrants(2,3,4,6)
    False
    """
    return not ont_intersection_vide(deb1, fin1, deb2, fin2)



### Roulette
def est_gagnant(bille:int , pari:str)->bool:
    """ Renvoie le resultat

    Précondition :
    Exemple(s) :
    $$$ est_gagnant(20,'pair')
    True
    $$$ est_gagnant(3,'impair')
    True
    $$$ est_gagnant(17,'17')
    True
    $$$ est_gagnant(20,'impair')
    False
    """
    condition1=bille%2==0 and pari=='pair'
    condition2=bille%2!=0 and pari=='impair'
    condition3= str(bille)==pari
    return condition1 or condition2 or condition3
def est_divisible(parametre1:int,parametre2:int)->bool:
    """ Renvoie si parametre1 est divisible par parametre2

    Précondition :parametre2!=0
    Exemple(s) :
    $$$ est_divisible(24,2)
    True
    $$$ est_divisible(24,4)
    True
    $$$ est_divisible(24,5)
    False
    """
    return parametre1%parametre2==0
	
def est_bissextile(annee:int)->bool:
    """ Renvoie si l'annee est bissextile

    Précondition :
    Exemple(s) :
    $$$ est_bissextile(2019)
    False
    $$$ est_bissextile(2020)
    True
    $$$ est_bissextile(2023)
    False
    $$$ est_bissextile(2000)
    True
    """
    par_quatre=est_divisible(annee,4)
    par_cent=est_divisible(annee,100)
    par_quatre_cent=est_divisible(annee,400)
    return (par_quatre and not par_cent) or  par_quatre_cent
