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

def main():
    lvaleur_int=list(range(2,10))
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
    
if __name__ == '__main__':
    main()
from math import pi,sqrt,cos
#3 Écriture de formules mathématique
#a= 1/2𝜋√𝐿𝐶
# en python a=1/2*pi*sqrt(L*C)
#b=𝑐𝑜𝑠e4(𝑎)
#b=cos(a)**4
#4.1: x=0,y=4
# a. (not x < -2) and (y >= 10 or 3 < 2 or y < 7)
#True
# b. x > 0 and 1/x > 10
# False
# c. (11%4) / (15//7)
#1.5
#4 Compréhension de code
#4.2.1:x=8
# if x < 5: #1 False
# TAUX = 3 #2 pas executer
# elif x < 10: #3 True
# cte1 = 2 #4 executer
# elif x < 15: #5 pas executer
# cte1 = 1 #6 pas executer
# else: #7 pas executer
# cte1 = 0 #8 pas executer
# x = x + cte1 #9 executer x=10
#4.2.2:x=0
# if x < 5: #1 True
# TAUX = 3 #2 executer
# elif x < 10: #3 pas executer
# cte1 = 2 #4 pas executer
# elif x < 15: #5 pas executer
# cte1 = 1 #6 pas executer
# else: #7 pas executer
# cte1 = 0 #8 pas executer
# x = x + cte1 #9 executer nameError: cte1 not defined
#4.3 Reecrire les codes
# 4.3.1
#if incorrect:
#   cpt = cpt
# else:
#   cpt = cpt + 1
#correction
#if not incorrect:
#   cpt = cpt + 1
#4.3.2
# res = ''
# if c.isdigit() == True:
#    res = res + c
#correction
# res = ''
# if c.isdigit():
#    res = res + c
#4.3.3
# def foo(n : int) -> bool:
# if n >= 0:
#   return True
# else:
#   return False
#correction
# def foo(n : int) -> bool:
#   return n >= 0
#4.4
# def mystere(chaine:str, car:str) -> str:
# """ Précondition : len(car) == 2 """
# res = '' #1
# k = 0 #2
# for elem in chaine[0:len(chaine)-1]: #3
# res = res + elem + car[k] #4
# k = 1 - k #5
# if len(chaine) > 0: #6
# res = res + chaine[len(chaine)-1] #7
# return res #8
#4.4.1 mystere('bio', '59')
#chaine[0:len(chaine)-1]='bi'
#chaine[len(chaine)-1]='b'
#car[0]=5
#car[1]=9
#4.4.2 mystere('bio', '59')
#appel de cette fonction est egal:'bi5b'
#4.4.2 mystere('s', '89')
#appel de cette fonction est egal:'8s'
#4.4.2 mystere('', '89')
#appel de cette fonction affiche :error indexation



