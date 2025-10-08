# Compléter ici (noms, groupe, contenu fichier, date)
#SOW Mamadou Radjaye ,MI23 , fonction_tva_traitre
#
#
#
# Ne pas supprimer cette ligne. <trace>tva_sem2.py</trace>

#################
# 2. TVA et prix
#################
TAUX_NORMAL=20.0
TAUX_REDUIT1=10.0
TAUX_REDUIT2=5.5
TAUX_PARTICULIER=2.1

def montant_tva(montant_ht:float, taux_tva:float)->float:
    """ Renvoie le montant tva

    Précondition : 
    Exemple(s) :
    $$$ montant_tva(10.5,TAUX_NORMAL)
    approx(2.1,1e-2)
    $$$ montant_tva(10.5,TAUX_REDUIT1)
    approx(1.05,1e-2)
    $$$ montant_tva(10.5,TAUX_REDUIT2)
    approx(0.57,1e-2)
    $$$ montant_tva(10.5,TAUX_PARTICULIER)
    approx(0.22,1e-2)
    """
    return montant_ht*(taux_tva/100)
    
from math import floor

def nb_euros(montant:float)->float:
    """ Renvoie le nombre d'euros

    Précondition : montant>1.0
    Exemple(s) :
    $$$ nb_euros(12.4)
    12
    """
    return floor(montant)
    


def nb_centimes(montant:float)->float:
    """Renvoie nombre de centimes

    Précondition :montant>1.0 
    Exemple(s) :
    $$$ nb_centimes(12.456)
    45
    """
    montant_cent=montant*100
    montant_finale=montant_cent%100
    return floor(montant_finale)
    
     

def formatage_tva(prix:float, taux_tva:float)->float:
    """ renvoie la une phrase
    Précondition : 
    Exemple(s) :
    $$$ formatage_tva(56, 2.1)
    "La tva à 2.1% sur 56 euros est de 1 euros et 17 centimes"
    """
    montant_tva_finale=montant_tva(prix,taux_tva)
    nb_euros_finale=nb_euros(montant_tva_finale)
    nb_centime= nb_centimes(montant_tva_finale)
    
    return f'La tva à {taux_tva}% sur {prix} euros est de {nb_euros_finale} euros et {nb_centime} centimes'
    


