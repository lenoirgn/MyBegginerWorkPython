# Compléter ici (noms, groupe, contenu fichier, date)
#Mamadou Radjaye sow, MI23,Mon traite_minute,Le 12/09/2025
#
#
#
# Ne pas supprimer cette ligne. <trace>minutes_sem2.py</trace>
NB_MINUTES_PAR_HEURE=60
NB_HEURES_PAR_JOUR=24

def heures_en_minutes(nb_heure:int)->int:
    """ Renvoie le nombre de minute
    Précondition :heure>0 
    Exemple(s) :
    $$$ heures_en_minutes(2)
    120
    """
    return nb_heure*NB_MINUTES_PAR_HEURE
    


def jours_en_heures(nb_jour:int)->int:
    """ Renvoie le nombre d'heures

    Précondition : jour>0
    Exemple(s) :
    $$$ jours_en_heures(2)
    48
    """
    return nb_jour*NB_HEURES_PAR_JOUR


def en_minutes(nb_jours:int, nb_heures:int, nb_minutes:int)->int:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : nb_jours>=0,nb_heures>=0 et nb_minutes>0
    Exemple(s) :
    $$$ en_minutes(1,2,3)
    1563
     """
    jour_en_heures=jours_en_heures(nb_jours)
   
    heure_en_minutes=heures_en_minutes( nb_heures+jour_en_heures)
    nb_minutes_finale= heure_en_minutes+nb_minutes
    return nb_minutes_finale
    

# Décommenter et compléter la signature donnée puis faire la suite
def formate_minutes(nb_minutes:int)->str:
    """ Renvoie le nombre de jours,heures et minutes

    Précondition : nb_minutes>0
    Exemple(s) :
    $$$ formate_minutes(1563)
    "1563 minutes contiennent 1 jours, 2 heures et 3 minutes"
    """
    nb_heures,nb_minutes_finale =divmod(nb_minutes,NB_MINUTES_PAR_HEURE)
    nb_jours,nb_heures_finale=divmod(nb_heures,NB_HEURES_PAR_JOUR)
    return f'{nb_minutes} minutes contiennent {nb_jours} jours, {nb_heures_finale} heures et {nb_minutes_finale} minutes'



