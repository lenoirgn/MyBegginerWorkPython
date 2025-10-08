# Compléter ici (noms, groupe, contenu fichier, date)
# Mamadou Radjaye sow, MI23,Mon Traitre_TD,Le 07/09/2025
#
#
#
# Ne pas supprimer cette ligne. <trace>fonctions_simples.py</trace>

################
# 1 - Répétition
################
def repetition(chaine:str, n:int)-> str:
    """ Renvoie la repetion du chaine de caractere

    Précondition :n>0 
    Exemple(s) :
    $$$ repetition('no',2)
    'nono'
    """
    return chaine*n
    

################
# 2 - Triangle
################

def perimetre_triangle(cote1:int, cote2:int, cote3:int)-> int:
    """ Renvoie le perimetre d'un triangle

    Précondition : cote1>0; cote2>0; cote3>0 ,
                   cote1+cote2>=cote3
                   cote1+cote3>=cote2
                   cote3+cote2>=cote1
    Exemple(s) : 
    $$$ perimetre_triangle(3,4,7)
    14
    """
    return cote1+cote2+cote3
    

################
# 3 - Promo
################

def prix_apres_promo(prix:float, remise:float)->float:
    """ Renvoie un prix promo

    Précondition : prix >0.0 ; remise >0.0
    Exemple(s) :
    $$$ prix_apres_promo(25.23,0.3)
    approx(17.66,1e-2)
    """
    return round(prix -(remise*prix),2)
    

#################
# 4 - Salutation
#################


def message_salutation(salutation:str, metier:str)-> str :
     """ Renvoie une chaine de caractere de salutation

     Précondition : salutation != '' et metier !=''
     Exemple(s) :
     $$$ message_salutation('salut', 'etudiant')
     'salut je suis etudiant'
     
     """
     return salutation +' je suis '+ metier
     

################
# 5 - Calcul de moyenne pondérée
################


def moyenne_entiere_ponderee(note1:int, coeff1:int, note2:int, coeff2:int)->int:
    """ Renvoie la moyenne entiere ponderee
    Précondition : coeff1>0 et coeff2>0
    Exemple(s) :
    $$$ moyenne_entiere_ponderee(10,3,12,2)
    10
    """
    return ((note1*coeff1)+(note2*coeff2))//(coeff1+coeff2)
    

################
# 6 - Température 
################


def conversion_fahrenheit(celsius:float)-> float:
     """ Renvoi la temperature en fahrenheit 

     Précondition :celsius> -273.15
     Exemple(s) :
     $$$ conversion_fahrenheit(24)
     75.2
     """
     return round( (9/5)*celsius + 32,2)
