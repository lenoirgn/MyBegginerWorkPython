# Compléter ici (noms, groupe, contenu fichier, date)
#Mamadou Radjaye sow, MI23,Mon traite_masque,Le 12/09/2025
#
#
#
# Ne pas supprimer cette ligne. <trace>minutes_sem2.py</trace>
from math import floor
def masque(valeur:int)->str:
    """ Renvoie l'entier masque

    Précondition : 1000<valeur<9999
    Exemple(s) :
    $$$ masque(2004)
    '2**4'
    """
    premier_chiffre=floor(valeur/1000)
    dernier_chiffre=valeur%1000
    return f"{ premier_chiffre}**{dernier_chiffre}"
    