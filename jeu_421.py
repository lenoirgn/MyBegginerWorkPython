# Compléter ici (noms, groupe, contenu fichier, date)
# Mamadou Radjaye sow MI23 , Traitre_jeu421 sur git ,le 03/10/2025
#
#
#
# Ne pas supprimer cette ligne. <trace>jeu_421.py</trace>

####### fonctions d'affichage

def affiche_congratulation():
    """ Affiche Bravo
    Précondition :
    Exemple(s) :
    $$$ 
    """
    print("Bravo! vous avez reussi")

def affiche_perdant():
    """ Affiche perdu
    Précondition :
    Exemple(s) :
    $$$ 
    """
    print("Ouf! vous n'avez pas reussi ")

def affiche_presentation_jeu(nom_joueur:str):
    """ affiche la presentation du jeu
    Précondition :
    Exemple(s) :
    $$$ 
    """
    print(f"{nom_joueur}, bienvenue au jeu du 421 !")
    print("Lancez les dés et tentez d'obtenir 421.")
    
    
def affiche_motif():
    """ Affiche le motif
    Précondition :
    Exemple(s) :
    $$$ 
    """
    print('+---+\t'*3)
    
def affiche_lancer(valeur1:int,valeur2:int, valeur3:int):
    """ Affiche la presentation du jeu
    Précondition :
    Exemple(s) :
    $$$ 
    """
    affiche_motif()
    print(f'| {valeur1} |\t| {valeur2} |\t| {valeur3} |\t')
    affiche_motif()
    

####### fonctions de saisie

def saisie_continuation()->str:
    """ Prend l'avis du jour
    Précondition :
    Exemple(s) :
    $$$ 
    """
    avis= input('Souhaitez-vous tenter votre chance ? y/n. ')
    return avis
    

def saisie_pseudo()->str:
    """
    Précondition :
    Exemple(s) :
    $$$ 
    """
    nom=input('Entrez votre pseudo : ')
    return nom
    

####### fonctions de calcul

from random import randint 
def lancer_de()-> int:
    """ Renvoie la une valeur aleatoire
    Précondition :
    Exemple(s) :
    $$$
    """
    return randint(1,6)
def est_42(valeur1:int ,valeur2:int )->bool:
    """ Renvoie true si la valeur est 42
    Précondition :
    Exemple(s) :
    $$$ est_42(2,4)
    False
    $$$ est_42(4,2)
    True
    """
    fin=str(valeur1)+str(valeur2)
    if fin=='42':
       return True
    else:
      return False
    
def est_421(lancer_de1:int,lancer_de2:int,lancer_de3:int)->bool:
    """ Renvoie true si la valeur est 421

    Précondition :
    Exemple(s) :
    $$$ est_421(2,3,4)
    False
    $$$ est_421(4,2,1)
    True
    $$$ est_421(4,2,2)
    False
    $$$ est_421(4,1,2)
    False
    """
    return est_42(lancer_de1,lancer_de2) and lancer_de3==1
       
    
       
       
    
    
def message_aurevoir():
    
    print('A une prochaine fois peut-être !')
    
def veut_continuer():
    """
    Précondition :
    Exemple(s) :
    $$$ 
    """
    avis=saisie_continuation()
    return avis=='y'
       
    
    

###### programme principal
if __name__=='__main__':
 joueur=saisie_pseudo()
 affiche_presentation_jeu(joueur)
 
 
 if veut_continuer():
    de1=lancer_de()
    de2=lancer_de()
    de3=lancer_de()
    affiche_lancer(de1,de2,de3)
    
    if est_421(de1,de2,de3):
       affiche_congratulation()
    else:
         affiche_perdant()
 else:
     message_aurevoir()
  
      
        
       
    
    
 
