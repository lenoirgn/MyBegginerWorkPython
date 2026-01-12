# Compléter ici (noms, groupe, contenu fichier, date)
# Mamadou Radjaye sow ,MI23, Mon traite de TD, 07/09/2025
#
#
#
# Ne pas supprimer cette ligne. <trace>fonctions_simples_compl.py</trace>

################
# 1 - Géométrie
################

def perimetre_quadrilatere(cote1:int,cote2:int,cote3:int,cote4:int)-> int:
    """ Renvoie perimetre d'un quadrilatere
    Précondition : cote1>0, cote2>0, cote3>0, cote4>0,
    Exemple(s) :
    $$$ perimetre_quadrilatere(2,4,5,7)
    18
    """
    return cote1 +cote2+cote3 +cote4
    

def aire_triangle(base:float,hauteur:float)->float:
    """ Renvoie l'aire du triangle
    Précondition : base>0.0 et hauteur>0.0
    Exemple(s) :
    $$$ aire_triangle (2,5)
    5
    """
    return 1/2*base*hauteur
    

################
# 2 - Éternuement
################

def eternuement(nb_a:int, nb_excl:int)-> str:
    """ Renvoie une onomatopée
    Précondition :nb_a>0  
    Exemple(s) :
    $$$ eternuement(4,3)
    'aaaatchoum!!!'
    """
    return (nb_a*'a')+'tchoum'+ (nb_excl*'!')
    
