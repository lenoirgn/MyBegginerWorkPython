# Compléter ici (noms, groupe, contenu fichier, date)
#Mamadou Radjaye sow MI23,fonctions, 11/09/2025
#
#
#
# Ne pas supprimer cette ligne. <trace>calculs_sem2.py</trace>

###################
# 1. Calculs
###################


def energie_cinetique(masse:int, x1:int, x2:int, temps:int)->int:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ energie_cinetique(20, 90, -10, 50)
    40
    """
    distance=(x2-x1)
    vitesse=distance/temps
    return 1/2*masse*vitesse**2
    

    
from math import pi
def aire_cercle(rayon:int)->float:
    """ Renvoie l'aire du cercle

    Précondition :rayon>0 
    Exemple(s) :
    $$$ aire_cercle(2)
    approx(12.56,1e-2)
    """
    return pi*rayon**2

 
def surface_couronne(rayon_ext:int, rayon_int:int)->float:
    """ Renvoie l'air de la couronne

    Précondition : rayon_exit>rayon_int
    Exemple(s) :
    $$$ surface_couronne(4,2)
    approx(37.69,1e-2)
    """
    return pi*(rayon_ext**2-rayon_int**2)
    
from math import tan

def cos_double(angle:int)->float :
    """ renoie le double cos de l'angle

    Précondition : 
    Exemple(s) :
    $$$ cos_double(pi)
    1
    """
    tang_carre = tan(angle)**2
    return (1-tang_carre)/(1+tang_carre)
