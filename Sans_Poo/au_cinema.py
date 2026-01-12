#Compléter ici (noms, groupe, contenu fichier, date)
#Mamadou Radjaye sow,MI23, Traite_au_cinema,21/09/2025
#
#
#
# Ne pas supprimer cette ligne. <trace>au_cinema.py</trace>

####################
# Au cinéma
####################
from datetime import date

def est_strict_anterieure_a(jour1:int, mois1:int, annee1:int, jour2:int, mois2:int, annee2:int)->bool:
    """ Renvoie si l'anne est anterieur
    Précondition :
    Exemple(s) :
    $$$ est_strict_anterieure_a(31, 12, 2022, 31, 12, 2022)
    False
    $$$ est_strict_anterieure_a(31, 12, 2022, 1, 1, 2023)
    True
    $$$ est_strict_anterieure_a(31, 12, 2022, 1, 1, 2022)
    False
    $$$ est_strict_anterieure_a(1, 1, 2022, 12, 12, 2021)
    False
    $$$ est_strict_anterieure_a(1, 1, 2022, 1, 12, 2022)
    True  
"""
    condition1= annee1<annee2
    condition2= annee1==annee2 and mois1<mois2
    condition3 = annee1==annee2 and mois1==mois2 and  jour1<jour2
    return condition1 or condition2 or condition3 

AGE_MAJORITE=18

def est_mineur_a_date(jour_naissance:int, mois_naissance:int, annee_naissance:int, jour:int, mois:int, annee:int)->bool:
    """ Renvoie si la personne est mineur

    Précondition :
    Exemple(s) :
    $$$ est_mineur_a_date(1, 1, 2013, 1, 1, 2013+AGE_MAJORITE)
    False
    $$$ est_mineur_a_date(12, 10, 2013, 1, 1, 2013+AGE_MAJORITE+3)
    False
    $$$ est_mineur_a_date(1, 1, 2013, 4, 7, 2013+AGE_MAJORITE-2)
    True
    """
    annee_de_la_majorite=annee_naissance+AGE_MAJORITE
    return  est_strict_anterieure_a(jour,mois,annee,jour_naissance,mois_naissance,annee_de_la_majorite) 

AGE_SENIOR=64

def est_senior_a_date(jour_naissance:int, mois_naissance:int, annee_naissance:int, jour:int, mois:int, annee:int)->bool:
    """ Renvoie si la personne est senior
    Précondition :
    Exemple(s) :
    $$$ est_senior_a_date(1, 1, 2013, 1, 1, 2013+AGE_SENIOR)
    True
    $$$ est_senior_a_date(1, 1, 2013, 1, 1, 2013+AGE_SENIOR+3)
    True
    $$$ est_senior_a_date(1, 1, 2013, 1, 1, 2013+AGE_SENIOR-2)
    False
    """
    annee_de_senior=annee_naissance+AGE_SENIOR
    return not est_strict_anterieure_a(jour,mois,annee,jour_naissance,mois_naissance,annee_de_senior) 


def a_tarif_reduit_a_date(jour_naissance:int, mois_naissance:int, annee_naissance:int, jour:int, mois:int, annee:int)->bool:
    """ Renvoie si la personne est eligible au reduit

    Précondition :
    Exemple(s) :
    $$$ a_tarif_reduit_a_date(1, 1, 2013, 1, 1, 2013+AGE_SENIOR)
    True
    $$$ a_tarif_reduit_a_date(1, 1, 2013, 1, 1, 2013+AGE_SENIOR-2)
    False
    $$$ a_tarif_reduit_a_date(1, 1, 2013, 1, 1, 2013+AGE_MAJORITE)
    False
    $$$ a_tarif_reduit_a_date(1, 1, 2013, 4, 7, 2013+AGE_MAJORITE-2)
    True
    """
    
    return  est_mineur_a_date(jour_naissance,mois_naissance,annee_naissance,jour,mois,annee) or \
		    est_senior_a_date(jour_naissance,mois_naissance,annee_naissance ,jour,mois,annee)  
	
def a_tarif_reduit(jour_naissance:int, mois_naissance:int, annee_naissance:int)->bool:
    """ Renvoie si la personne est eligible au reduit aujourd'hui

    Précondition :
    Exemple(s) :
    $$$ a_tarif_reduit(1, 1, 2013)
    True
    $$$ a_tarif_reduit(1, 1, 2004)
    False
    $$$ a_tarif_reduit(1, 1, 19960)
    True
    """
    aujourdhui = date.today()
    jour=aujourdhui.day
    mois =aujourdhui.month
    annee=aujourdhui.year
    return a_tarif_reduit_a_date(jour_naissance,mois_naissance,annee_naissance,jour,mois,annee)
# à vous de jouer !
