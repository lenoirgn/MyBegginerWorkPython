# Compléter ici (noms, groupe, contenu fichier, date)
#
#
#
#
# Ne pas supprimer cette ligne. <trace>sequences_indexation.py</trace>


####################
# Parcours de sous-listes ou sous-chaines, éventuellement avec un pas
####################


def echantillonne(n:int, chaine:str)->str:
    """ Renvoie un echantillon
    Précondition : 
    Exemple(s) :
    $$$ echantillonne(3, 'azertyuiop')
    'arup'
    $$$ echantillonne(3, '')
    ''
    """
    return chaine[::n]


def elements_indices_impairs(lchaine:list[int])->list:
    """ Renvoie les element a indice impaire
    Précondition : 
    Exemple(s) :
    $$$ elements_indices_impairs([10, 24, 12, 2, 14, 15, 16])
    [24, 2, 15]
    $$$ elements_indices_impairs([])
    []
    """
    return lchaine[1::2]
    


def miroir_pas(chaine:str)->str:
    """ 
    Précondition : 
    Exemple(s) :
    $$$ miroir_pas('azerty')
    'ytreza'
    """
    return chaine[::-1]
    


def minimum(lentiers:list[int])->int:
    """ Renvoie le min

    Précondition : 
    Exemple(s) :
    $$$ minimum([10, 24, 12, 2, 14, 15, 16])
    2
    $$$ minimum([10, 24, 12, 2, 14, 15, 1])
    1
    $$$ minimum([0, 24, 12, 2, 14, 15, 1])
    0
    $$$ minimum([1])
    1
    """
    mini=lentiers[0]
    for entier in lentiers:
        if entier<mini:
            mini=entier
        
    return mini


####################
# Variable locale à réinitialiser
####################


def decoupage(chaine:str, separateurs:str)-> list[str]:
    """ Renvoie la liste des mots separer
    Précondition :
    Exemple(s) :
    $$$ decoupage('Tu as fini tes devoirs ? Non, pas encore.', ',.; !?')
    $$$ decoupage('', ',.; !?')
    []
    ['Tu', 'as', 'fini', 'tes', 'devoirs', '', '', 'Non', '', 'pas', 'encore', '']
    $$$ decoupage('Tu as fini tes devoirs ? Non, pas encore.', ',;  !?')
    ['Tu', 'as', 'fini', 'tes', 'devoirs', '', '', 'Non', '', 'pas', 'encore.']
    $$$ decoupage('Tu as fini tes devoirs ? Non, pas encore!!', ',;.  !?')
    ['Tu', 'as', 'fini', 'tes', 'devoirs', '', '', 'Non', '', 'pas', 'encore', '','']
    $$$ decoupage('@Tu as fini tes devoirs ? Non, pas encore!!', ',;@.  !?')
    ['','Tu', 'as', 'fini', 'tes', 'devoirs', '', '', 'Non', '', 'pas', 'encore', '','']
    """
    temp_mot=''
    lres=[]
    for mot in chaine:
        if mot in separateurs:
           lres.append(temp_mot)
           temp_mot=''
        else:
           temp_mot+=mot
    if chaine != '':
      if chaine[-1] in separateurs:
         lres.append('')
      else:
        lres.append(temp_mot)
    return lres

    

####################
# Paires d'éléments consécutifs
####################


def premieres_occurrences(chaine:str)->str:
    """ Renvoie l'unique occurrence
    Précondition :
    Exemple(s) :
    $$$ premieres_occurrences("aabbbaabcdd")
    'ababcd'
    $$$ premieres_occurrences("aaa")
    'a'
    $$$ premieres_occurrences("")
    ""
    """
    reschaine=''
    if chaine !='':
       precedent=chaine[0]
       reschaine=chaine[0]
       for car in chaine[1:]:
           if car != precedent:
              reschaine+=car
              precedent=car
    return reschaine
    
       
       

####################
# Boucles imbriquées
####################

def matchs(lequipe1:list[str],lequipe2:list[str])->list[str]:
    """ Renvoie liste de match
    Précondition :
    Exemple(s) :
    $$$ matchs(['Losc', 'RC Lens'], \
    ['Stade Rennais', 'FC Lorient', 'Stade Brestois'])
    ['Losc contre Stade Rennais', \
    'Losc contre FC Lorient', \
    'Losc contre Stade Brestois', \
    'RC Lens contre Stade Rennais', \
    'RC Lens contre FC Lorient', \
    'RC Lens contre Stade Brestois']
    $$$ matchs(['Losc'], \
    ['Stade Rennais', 'FC Lorient', 'Stade Brestois'])
    ['Losc contre Stade Rennais', \
    'Losc contre FC Lorient', \
    'Losc contre Stade Brestois']
    """
    lres=[]
    for equipe1 in lequipe1:
        for equipe2 in lequipe2:
            lres.append(f'{equipe1} contre {equipe2}')
    return lres
    

####################
# En vrac
####################

def nom_domaines(lextensions:list[str], ldomaines:list[str]):
    """ Renvoie le nom de dommaine

    Précondition :
    Exemple(s) :
    $$$ nom_domaines (['fr', 'net', 'eu'], ['mondomaine', 'mon_domaine_a_moi'])
    ['www.mondomaine.fr','www.mondomaine.net','www.mondomaine.eu','www.mon_domaine_a_moi.fr','www.mon_domaine_a_moi.net','www.mon_domaine_a_moi.eu']
    """
    lres=[]
    for domaine in ldomaines:
        for extensions in lextensions :
           lres.append(f'www.{domaine}.{extensions}')      
    return lres
            
    


def max_identiques(lentiers:list[int])->int:
    """ Renvoie le max identique

    Précondition :
    Exemple(s) :
    $$$ max_identiques([1, 2, 2, 2, 1, 6, 6, 5])
    3
    $$$ max_identiques([1, 2, 2, 1, 6, 6,6, 5])
    3
    $$$ max_identiques([1,1])
    2
    $$$ max_identiques([])
    0
    $$$ max_identiques([1])
    1
    $$$ max_identiques([1,3,4,6,7])
    1
    """
    maxi=1
    maxiFin=0
    if lentiers !=[]:
       entier_prec=lentiers[0]
       for entier in lentiers[1:]:
         if entier==entier_prec:
              maxi+=1
              if maxi>maxiFin:
                 maxiFin=maxi
                 maxi=1
         else:
                entier_prec=entier
       if maxi>maxiFin:
                 maxiFin=maxi
         
         
    return maxiFin

               
def suffixes(mot:str)->list[str]:
    """ Renvoie la lsite de suffixes

    Précondition :
    Exemple(s) :
    $$$ suffixes('fin')
    ['', 'n', 'in', 'fin']
    $$$ suffixes('')
    []
    $$$ suffixes('a')
    ['','a']
    """
    temp_suffixe =''
    lsuffixe=['']
    if mot !='':
       for suffixe in mot[::-1]:
           temp_suffixe=suffixe+temp_suffixe
           lsuffixe.append(temp_suffixe)
    else:
        lsuffixe=[]
    return lsuffixe
       
    
   


def resume(chaine:str)->str:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ resume("abbbaabc")
    '1a3b2a1b1c'
    $$$ resume("c")
    '1c'
    
    """
    reschaine=''
    comp=1
    if chaine !='':
       precedent=chaine[0]
       reschaine=''
       for car in chaine[1:]:
           if car != precedent:
              reschaine+=f"{comp}{precedent}"
              precedent=car
              comp=1
           else:
               comp+=1
       reschaine+=f"{comp}{precedent}"
    return reschaine

def ajout_separateur(liste:list[str], sep:str)->str:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ ajout_separateur(['vrai ?'], '*')
    'vrai ?'
    $$$ ajout_separateur(['est','il'], '-')
    'est-il'
    $$$ ajout_separateur(["n'est", 'il', 'pas', 'vrai ?'], '-')
    "n'est-il-pas-vrai ?"
    """
    reschaine=liste[0]
    for elmt in liste[1:]:
       reschaine+=f"{sep}{elmt}"
    return reschaine

def construit_mots(lmot1:list[str], lmot2:list[str])->list[str]:
    """ Renvoie une liste de mot de construit

    Précondition :
    Exemple(s) :
    $$$ construit_mots(["ta", "meu"], ["ble", "re", "le"])
    ["table", 'bleta', 'tare', 'reta', 'tale', 'leta', 'meuble', 'blemeu', 'meure', 'remeu', 'meule', 'lemeu'] 
    """
    lres=[]
    for mot1 in lmot1:
       for mot2 in lmot2:
           lres.append(f"{mot1}{mot2}")
           lres.append(f"{mot2}{mot1}")
    return lres

########################
# Zorglang
######################
def zorglangue(chaine:str)->str:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ zorglangue('salut ça va ?')
    'tulas aç av ?'
    $$$ zorglangue('salut toi !?')
    'tulas iot ?!'
    """
    chaine_a_inverser=''
    chaine_temp=''
    esp=' '
    reschaine=''
    for car in chaine:
      if car==esp:
         chaine_a_inverser=chaine_temp
         chaine_inverse=miroir_pas(chaine_a_inverser)
         reschaine+=chaine_inverse+esp
         chaine_temp=''
      else:
         chaine_temp+=car
    reschaine+=miroir_pas(chaine_temp)
    return reschaine
        
          
    

    


if __name__ == '__main__':

    phrase=input('Entrer une phrase en minuscules : ')
    phrase_en_zorglangue=zorglangue(phrase)
    print(f'Voici sa traduction en zorglang : {phrase_en_zorglangue}')