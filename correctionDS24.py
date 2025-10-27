def moyenne_colles(lentier:list[int])->float:
    """Renvoie la moyenne
    Précondition :lentier!=[],1<=entier and entier<=4 
    Exemple(s) :
    $$$ moyenne_colles([1,3,2])
    2.0
    """
    somme=0
    for entier in lentier:
        somme+=entier
    return somme/len(lentier)
def nb_fortes_colles(lentier:list[int])->int:
    """ Nombre d'element >=3

    Précondition : 
    Exemple(s) :
    $$$ nb_fortes_colles([3,1,4,2])
    2
    $$$ nb_fortes_colles([1,2,1,2])
    0
    """
    cumul=0
    for entier in lentier:
        if entier>=3:
          cumul+=1  
    return cumul
def message(lentier:list[int])->str:
    """ Renvoie le message 

    Précondition : 
    Exemple(s) :
    $$$ message([])
    ''
    $$$ message([3,4])
    'collé occasionnellement pour des comportements très inadapté'
    $$$ message([1,2,1,1,1])
    'collé fréquemment'
    """
    if len(lentier)==0:
        res = ''
    elif len(lentier)>0:
        res='collé'
        if len(lentier) in [2,3]:
            res+=' '+'occasionnellement'
        elif len(lentier) in [4,5,6]:
            res+=' '+'fréquemment'
        elif len(lentier)>=7:
            res+=' '+'très souvent'
        if moyenne_colles(lentier)>=3:
            res+=' '+'pour des comportements très inadapté'
    return res
            
def est_rouge(carte:str)->bool:
    """Renvoie true 

    Précondition : 
    Exemple(s) :
    $$$ est_rouge('3H')
    True
    $$$ est_rouge('9S')
    False
    """
    return 'H' in carte or 'D' in carte

def est_paire_valide(carte1:str,carte2:str)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ est_paire_valide('2H', '9C')
    True
    $$$ est_paire_valide('2H', '9D')
    False
    $$$ est_paire_valide('3H', '7S')
    True
    $$$ est_paire_valide('6H', '2D')
    False
    $$$ est_paire_valide('4H', '5C')
    False
    """
    somme= int(carte1[0])+int(carte2[0])
    difference=abs(int(carte1[0])-int(carte2[0]))
    ok_valeur=(somme==11 or difference==4)
    return (est_rouge(carte1) and not est_rouge(carte2) or \
           est_rouge(carte2) and not est_rouge(carte1)) and \
           ok_valeur
    
def  genere_paquet(lvaleur:list[str],lcouleur:list[str])->list[str]:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ genere_paquet(['2', '3', '4', '5'], ['D', 'H'])
    ['2D', '3D', '4D', '5D', '2H', '3H', '4H', '5H']
    """
    lres=[]
    for couleur in lcouleur:
        for valeur in lvaleur:
            lres.append(valeur+couleur)
    return lres 
            
def separe_paquet(lcarac:list[str])->list[str]:
     """ 

     Précondition : 
     Exemple(s) :
     $$$ separe_paquet(['D', 'D', 'S', 'C', 'C', 'C', 'D'])
     ['DD', 'S', 'CCC', 'D']
     $$$ separe_paquet(['D', 'S', 'C'])
     ['D', 'S', 'C']
     $$$ separe_paquet(['D', 'D', 'D'])
     ['DDD']
     $$$ separe_paquet([])
     []
     
     """
     lres=[]
     if lcarac!=[]:
         prec=lcarac[0]
         temp=lcarac[0]
         for carac in lcarac[1:]:
             if carac!=prec:
                 lres.append(temp)
                 prec=carac
                 temp=carac
             else:
                temp+=carac
         lres.append(temp)
     return lres


if __name__ == '__main__':
    lvaleur_int=list(range(1,10))
    lvaleur_str=[]
    for valeur in lvaleur_int:
        lvaleur_str.append(str(valeur))
           
           
    lcouleur=['H','D','S','C']
    carte=genere_paquet(lvaleur_str,lcouleur)
    

    lindice=[]
    for i in range(2):
        indice=int(input("Entrer un indice dans le paquet de cartes : "))
        lindice.append(indice)
    if est_paire_valide(carte[lindice[0]],carte[lindice[1]]):
        print(f"{carte[lindice[0]]} et {carte[lindice[1]]} est une paire valide")
    else:
        print(f"{carte[lindice[0]]} et {carte[lindice[1]]} n'est une paire valide")
