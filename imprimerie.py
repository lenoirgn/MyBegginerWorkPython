# Compléter ici (noms, groupe, contenu fichier, date)
# Mamadou Radjaye sow MI23 , Traitre_imprimerie,le 03/10/2025
#
#
#
# Ne pas supprimer cette ligne. <trace>imprimerie.py</trace>

# Vous êtes libres d'utiliser les noms de fonction de votre choix. 
from math import ceil
def nombre_commandable(nb_souhaite:int,nb_commandable:int)->int:
    """ renvoie le nombre commandable

    Précondition :
    Exemple(s) :
    $$$ nombre_commandable(20,100)
    100
    """
    return ceil(nb_souhaite/nb_commandable)*nb_commandable

def nombre_exemplaires(nb_souhaite:int)->int:
    """ Renvoie le nombre commandable

    Précondition :
    Exemple(s) :
    $$$ nombre_exemplaires(24)
    100
    $$$ nombre_exemplaires(204)
    500
    """
    if nb_souhaite <= 100:
       nombres_commandables = nombre_commandable(nb_souhaite, 100)
    elif nb_souhaite <= 500:
       nombres_commandables = nombre_commandable(nb_souhaite, 500)
    elif nb_souhaite <= 1000:
       nombres_commandables = nombre_commandable(nb_souhaite, 1000)
    elif nb_souhaite > 1000:
       nombres_commandables = nombre_commandable(nb_souhaite, 1000)

    return nombres_commandables

def montant_facture(nb_voulus:int)->float:
    """ Renvoie le montant de la facture

    Précondition :
    Exemple(s) :
    $$$ montant_facture(3000)
    90
    $$$ montant_facture(24)
    30
    $$$ montant_facture(450)
    45
    $$$ montant_facture(1460)
    60
    
    """
    nb_voulu=nombre_exemplaires(nb_voulus)
    if nb_voulu==100:
      montant= nb_voulu*0.30
    elif nb_voulu==500:
      montant= nb_voulu*0.09
    elif nb_voulu==1000:
      montant= nb_voulu*0.05
    elif nb_voulu>=2000:
      montant= nb_voulu*0.03
    return montant


def saisie_commande()->int:
    """ Renvoie le nombre commande
    Précondition : 
    Exemple(s) :
    $$$
    """
    nombre=int(input('Combien de flyers voulez-vous commander ? '))
    return nombre

def affichage(nombre_commande:int):
    """ affiche le nombre de commande 
    Précondition : 
    Exemple(s) :
    $$$ 
    """
    print(f'Nombre de flyers livrés : {nombre_commande}')
    
    
def affichage_montant(montant:float):
    """ affiche le montant a payer
    Précondition : 
    Exemple(s) :
    $$$ 
    """
    print(f'Montant (en euros) : {montant}')
    
    
    



if __name__ == '__main__':
    nombre_souhaite=saisie_commande()
    nombre_commandables=nombre_exemplaires(nombre_souhaite)
    montant=montant_facture(nombre_commandables)
    affichage(nombre_commandables)
    affichage_montant(montant)
    
    