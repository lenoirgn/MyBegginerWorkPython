# Compléter ici (noms, groupe, contenu fichier, date)
#Mamadou Radjaye sow,MI23, Traite_Predicat_simple,21/09/2025
#
#
#
# Ne pas supprimer cette ligne. <trace>predicats_simples.py</trace>

####################
# Premiers prédicats
####################
YES='oui'
NO='non'
AUCUN='je sais pas'

def est_non_vide(chaine:str)->bool:
    """ predicat de chaine vide ou non

    Précondition : 
    Exemple(s) :
    $$$ est_non_vide ('')
    False
    $$$ est_non_vide ('moi')
    True
    """
    return  len(chaine)!=0
    
    


def est_reponse(chaine:str)->bool:
    """ Renvoie une reponse

    Précondition : 
    Exemple(s) :
    $$$ est_reponse('oui')
    True
    $$$ est_reponse('non')
    True
    $$$ est_reponse('moi')
    False
    """
    return chaine == YES or chaine == NO


def est_beneficiaire(age:int, titulaire_permis:bool)-> bool:
    """ Renvoie l'elisibilite pour permis
    Précondition : 
    Exemple(s) :
    $$$ est_beneficiaire(18, False)
    True
    $$$ est_beneficiaire(18, True)
    False
    $$$ est_beneficiaire(30, False)
    False
    
    """
    return age >=15 and age <=25 and  not titulaire_permis
    


def est_reponse_correcte(n:int, reponse:str)->bool:
    """Renvoie le resultat de la reponse

    Précondition : 
    Exemple(s) :
    $$$ est_reponse_correcte(2,YES)
    True
    $$$ est_reponse_correcte(3,NO)
    True
    $$$ est_reponse_correcte(3,YES)
    False
    """
    return (n%2==0 and reponse == YES ) or (n%2!=0 and reponse == NO)

def est_semestre_valide(moy_BBC1:float,moy_BBC2:float)->bool:
    """ Renvoie le resultat du semestre

    Précondition : moy_BB1>0 et moy_BB2>0
    Exemple(s) :
    $$$ est_semestre_valide(10,9)
    False
    $$$ est_semestre_valide(18,9)
    True
    """
    return (moy_BBC1+moy_BBC2)/2>=10


def est_annee_validee(semestre1:bool,semestre2:bool)->bool:
    """ Renvoie le resultat de l'annee
    Précondition : 
    Exemple(s) :
    $$$ est_annee_validee(True,False)
    False
    $$$ est_annee_validee(True,True)
    True
    """
    return semestre1 and  semestre2
    

