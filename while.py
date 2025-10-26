# Compléter ici (noms, groupe, contenu fichier, date)
# Mamadou Radjaye sow MI23 Traite de while.py Le 22/10/2025
#
#
#
# Ne pas supprimer cette ligne. <trace>while.py</trace>


####################
# Utilisation de boucles while
####################

def nb_jours_avant_1m_blob(taille_init:float)->int:
    """ Renvoie le nombre de jours après lesquels le blob atteindra ou dépassera 1 mètre, partant de la taille initiale

    Précondition : 
    Exemple(s) :
    $$$ nb_jours_avant_1m_blob(0.5)
    1
    $$$ nb_jours_avant_1m_blob(1)
    0
    $$$ nb_jours_avant_1m_blob(2)
    0
    $$$ nb_jours_avant_1m_blob(0.125)
    3
    """
    nb_jour=0
    while taille_init < 1:
        nb_jour+=1
        taille_init*=2
    return nb_jour
        
    
    

def somme_chiffres(entier:int):
    """ Renvoie la somme de ses chiffres

    Précondition : 
    Exemple(s) :
    $$$ somme_chiffres(1234)
    10
    $$$ somme_chiffres(1)
    1
    $$$ somme_chiffres(0)
    0
    """
    somme=0
    while entier!=0:
        somme+=entier%10
        entier=entier//10
    return somme
    

def saisie_pseudo_avec_verification(pseudo:str)->str:
    """ Renvoie la dernière chaîne saisie

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    pseudo2=input("Saisir le second pseudo: ")
    while pseudo2==pseudo:
        pseudo2=input("Saisir le second pseudo: ")
    return pseudo2
        
        
    
