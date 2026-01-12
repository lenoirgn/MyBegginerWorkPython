def predicat1(x:int,y:int,n:int)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ predicat1(3, 5, 2)
    True
    $$$ predicat1(1, 5, 2)
    False
    """
    return 12*x==(1+y)**n
def predicat2(x:int,y:int,n:int)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ predicat2(3, 5, 2)
    True
    $$$ predicat2(1, 5, 2)
    False
    """
    return x>=(1+y)/n
    
def nb_points(lettre:str)->int :
    """ 

    Précondition : 
    Exemple(s) :
    $$$ nb_points('B')
    3
    $$$ nb_points('K')
    10
    """
    
    if lettre in [ 'A', 'E', 'I', 'L', 'N','O',' R', 'S', 'T', 'U']:
        nb_point=1
    elif lettre in [' D', 'G', 'M']:
        nb_point=2
    elif lettre in ['B','C','P']:
        nb_point=3
    elif lettre in [ 'F', 'H', 'V']:
        nb_point=4
    elif lettre in['J', 'Q']:
        nb_point=8
    else:
       nb_point=10
    return nb_point

def calcule_score(mot:str) ->int:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ calcule_score('HELLO')
    8
    $$$ calcule_score('ZEN')
    12
    """
    score=0
    for car in mot:
        score+=nb_points(car)
    return score
def plus_grand_score(mot1:str,mot2:str):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ plus_grand_score('HELLO', 'ZEN')
    'ZEN'
    """
    maxi=""
    if calcule_score(mot1)>calcule_score(mot2):
        maxi=mot1
    else:
        maxi=mot2
    return maxi
#Lecture du compte
# def mystere(n):
#     res = ''
#     for k in range(n, 0, -1):
#         res = res + str(k) + '-'
#     return res + '0'
#mystere(4)
#Avant la boucle:
#n=4
#res=''
#k n'est pas defini
#Apres la boucle
# res='4-3-2-1-0'


# 1. a = 10
# b = 20
# n = (a == b) or (b > a)
#1.n=True
# 2. n = 0
# for x in range(10, 21):
# n = 1 + n
#2.n=11
# 3. y == 3
# n = y - 1
#3.nameError
# 4. def addition(a, b):
# return a + b
# n = addition(addition(5, 4), 1) / 2
#4.n=5
# 5. n = len('Hello !')
# if n == 7:
# n = n + 1
# elif n == 8:
# n = n + 2
# else:
# n = n + 10
#n=8