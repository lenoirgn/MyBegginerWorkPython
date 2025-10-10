# Compléter ici (noms, groupe, contenu fichier, date)
#Mamadou Radjaye sow MI23 traite_iterable, le 10/10/2025
#
#
#
# Ne pas supprimer cette ligne. <trace>iterables_for.py</trace>


####################
# Algorithmes de traitement de listes
####################


def carres(lentiers:list[int])->list[int]:
    """ Renvoie le carre des element de la liste

    Précondition : 
    Exemple(s) :
    $$$ carres([2, 3, 5, 7])
    [4, 9, 25, 49]
    $$$ carres([])
    []
    """
    lres=[]
    for ele in lentiers:
        lres.append(ele**2)
    return lres
    


def nombre_occurrences(elt:int, lentiers:list[int])->int:
    """ Renvoie le nombre d'occurrence

    Précondition : 
    Exemple(s) :
    $$$ nombre_occurrences(2, [4, 2, 6, 2, 2, 5, 4])
    3
    $$$ nombre_occurrences(7, [4, 2, 6, 2, 2, 5, 4])
    0
    $$$ nombre_occurrences(7, [])
    0
    """
    nb_occu=0
    for entier in lentiers:
        if elt == entier:
            nb_occu+=1
    return nb_occu

def nombre_occurrences2(a_compter:list[int], liste:list[int])->int:
    """ 
    Renvoie le nombre d'occurrence
    Précondition : 
    Exemple(s) :
    $$$ nombre_occurrences2([4, 2, 7], [4, 2, 6, 2, 2, 5, 4])
    5
    $$$ nombre_occurrences2([1, 3, 9], [4, 2, 6, 2, 2, 5, 4])
    0
    """
    nb_occu=0
    for entier in liste:
        if  entier in a_compter:
            nb_occu+=1
    return nb_occu
    


def sans_element(x:int, liste:list[int])->list[int]:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ sans_element(3, [3, 0, 3, 3, -6, 12, -7, 3])
    [0, -6, 12, -7] 
    """
    lres=[]
    for ele in liste:
        if ele != x:
            lres.append(ele)
    return lres
    
    


def moyenne(liste:list[float])->float:
    """ Renvoie la moyenne

    Précondition : 
    Exemple(s) :
    $$$ moyenne([2, 3, 5, 7])
    4.25
    """
    
    somme=0
    for ele in liste:
        somme +=ele
        moyenne =somme/len(liste)
    return moyenne
      


def concatenation(lchaine:list[str])->str:
    """ Renvoie une chaine concatenee

    Précondition : 
    Exemple(s) :
    $$$ concatenation(["liste", "de", " chaines"])
    'listede chaines'
    $$$ concatenation([])
    ''
    """
    reschaine=''
    for ele in lchaine:
        reschaine +=ele
        
    return reschaine


def positive(liste:list[int])->list[int]:
    """ Renvoie une liste de positif

    Précondition : 
    Exemple(s) :
    $$$ positive([0, 3, -6, 12, -7])
    [0, 3, 6, 12, 7]
    $$$ positive([])
    []
    """
    lres=[]
    for ele in liste:
        if ele <0:
            ele *=-1
            lres.append(ele)
        else:
            lres.append(ele)
    return lres
    
    


def lg_max_chaines(liste:list[str])->int:
    """ Renvoie la longueurs max de chaine

    Précondition : 
    Exemple(s) :
    $$$ lg_max_chaines(['un', 'milieu max', 'trois'])
    10
    $$$ lg_max_chaines([])
    0
    """
    maxi=0
    for ele in liste:
        if len(ele)>maxi:
            maxi=len(ele)
        
    return maxi
    
    

####################
# Algorithmes de traitement de chaînes
####################


def chiffres(chaine:str):
    """ Renvoie uniquement les chiffres

    Précondition : 
    Exemple(s) :
    $$$ chiffres('7 et 8 octobre 2023')
    '782023'
    $$$ chiffres(' octobre ')
    ''
    """
    reschiffres=''
    for carac in chaine:
        if str.isdigit(carac):
            reschiffres+=carac
    return reschiffres
            
    


def miroir_for(chaine:str)-> str:
    """ Renvoie la chaine inversee

    Précondition : 
    Exemple(s) :
    $$$ miroir_for("Hello !")
    '! olleH'
    $$$ miroir_for("ici")
    'ici'
    $$$ miroir_for('')
    ''
    """
    reschaine=''
    for ele in chaine:
        reschaine=ele+reschaine
        
    return reschaine


def compte_2car(texte:str, car1:str, car2:str)->int:
    """ Renvoie le nombre d'occurrence

    Précondition :
    Exemple(s) :
    $$$ compte_2car('abracadabra', 'a', 'r')
    7
    $$$ compte_2car('abracadabra', 'v', 'g')
    0
    $$$ compte_2car('', 'v', 'g')
    0
    """
    nb_occu=0
    for carac in texte:
       if car1 == carac or car2 == carac:
             nb_occu += 1
    return nb_occu

####################
# Utilisation du type range
####################


def table_multiplication(entier:int):
    """ Renvoie une liste de multiple

    Précondition :
    Exemple(s) :
    $$$ table_multiplication(5)
    [5, 10, 15, 20, 25, 30, 35, 40, 45, 50] 
    """
    lres=[]
    for i in range(1,11):
       lres.append(entier*i)
    return lres



def saisie_liste(entier:int):
    """  Demande le nombre de siasie et renvoie la

    Précondition :
    Exemple(s) :
    $$$ 
    """
    lres=[]
    for i in range(entier):
       element= int(input("Entrer une valeur entiere : "))
       lres.append(element)
    return lres
    

####################
# Algorithmes qui changent un peu...
####################


def somme_cumulee(liste:list[int])->list[int]:
    """ Renvoie une liste de somme cumulee

    Précondition :
    Exemple(s) :
    $$$ somme_cumulee([1, 2, 5])
    [1, 3, 8]
    $$$ somme_cumulee([])
    []
    """
    lres=[]
    somme=0
    for ele in liste :
        somme+=ele
        lres.append(somme)
    return lres
       

def prefixes(mot:str)->list[str]:
    """ Renvoie les prefixes du mot donne
    Précondition :
    Exemple(s) :
    $$$ prefixes('motus')
    ['', 'm', 'mo', 'mot', 'motu', 'motus'] 
    """
    lres=['']
    prefixe=''
    for carac in mot:
        prefixe+=carac
        lres.append(prefixe)
        
    return lres



def insere_sauts_ligne(chaine:str, lg_ligne:int)->str:
    """ Renvoie un text avec des saut de ligne

    Précondition :
    Exemple(s) :
    $$$ insere_sauts_ligne("Je ne sais pas si des mots seront coupés.", 5)
    "Je ne\\n sais\\n pas \\nsi de\\ns mot\\ns ser\\nont c\\noupés\\n."
    """
    nouvelle_chaine=''
    somme=0
    for carac in chaine:
        nouvelle_chaine+=carac
        somme+=1
        if somme==lg_ligne:
           nouvelle_chaine+='\n'
           somme=0
    return nouvelle_chaine
 
##########################
# Écriture d’un programme principal
########################## 

if __name__ == '__main__':
   nb_ligne=int(input("Entrer le nombre d'elelmet: "))
   liste=saisie_liste(nb_ligne)
   liste_positive=positive(liste)
   print(f'Le résultat de positive {liste} est : {liste_positive}')
   