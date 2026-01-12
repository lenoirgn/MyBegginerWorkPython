from math import floor

def entier_pourcentage_realise(longueur:int,pourcentage:int):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ entier_pourcentage_realise(0, 50)
    0
    $$$ entier_pourcentage_realise(75, 66)
    49
    $$$ entier_pourcentage_realise(100, 100)
    100
    """
    return floor((longueur*pourcentage)/100)

def entier_pourcentage_restant(entier_realise:int,longueur:int):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ entier_pourcentage_restant(50, 100)
    50
    $$$ entier_pourcentage_restant(33, 100)
    67
    $$$ entier_pourcentage_restant(20, 80)
    60
    
    """
    return longueur-entier_realise


def barre1(longueur:int,pourcentage:int):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ barre1(20,40)
    '[40%][========............]'
    $$$ barre1(20, 0)
    '[0%][....................]'
    $$$ barre1(20, 100)
    '[100%][====================]'
    """
    car_realise='='
    car_restant='.'
    n=entier_pourcentage_realise(longueur,pourcentage)
    m=entier_pourcentage_restant(n,longueur)
    
    return f'[{pourcentage}%][{n*car_realise}{m*car_restant}]'
def barre2(longueur:int,pourcentage:int):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ barre2(20,40)
    '[40%][++++++++------------]'
    $$$ barre2(20, 0)
    '[0%][--------------------]'
    $$$ barre2(20, 100)
    '[100%][++++++++++++++++++++]'
    $$$ barre2(20, 50)
    '[50%][++++++++++----------]'
    """
    car_realise='+'
    car_restant='-'
    n=entier_pourcentage_realise(longueur,pourcentage)
    m=entier_pourcentage_restant(n,longueur)
    
    return f'[{pourcentage}%][{n*car_realise}{m*car_restant}]'