def saisir()->str:
    
    message=input("Entrez une phrase : ")
    return message

def phrase_en_liste(phrase:str)->list:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ phrase_en_liste('La mission 47290 progresse vers le succès !')
    ["La", "mission", "47290", "progresse", "vers", "le", "succès", "!"]

    """
    
    
    prec=''
    esp=' '
    lres=[]
    for car in phrase:
        if car ==esp:
            lres.append(prec)
            prec=''
        else:
            prec+=car
    lres.append(prec)
    return lres
def chiffrement_mot(mot:str,entier:int)->str:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ chiffrement_mot ('secret',2)
    'etsecr'
    
    """
    return mot[len(mot)-entier:]+mot[:len(mot)-entier]
    
def dechiffrement_mot(mot:str,entier:int)->str:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ dechiffrement_mot('etsecr',2)
    'secret'
    """
    return mot[entier:]+mot[0:entier]

def chiffrement_nombre(chaine:str)->str:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ chiffrement_nombre('1234')
    '9876'
    $$$ chiffrement_nombre('10234')
    '90876'
    """
    res=''
    for car in chaine:
        if car =='0':
            res+=car
        else:
            res+=str(10-int(car))
    return res

def chiffrement_list(lmot:list[str],entier:int)->list[str]:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ chiffrement_list(['La', 'mission', '47290', 'progresse', '!'], 2)
    ['La', 'onmissi', '63810', 'seprogres', '!']
    """
    lres=[]
    for mot in lmot:
        if mot.isdigit():
            lres.append(chiffrement_nombre(mot))
        else:
            lres.append(chiffrement_mot(mot,entier))
    return lres

def reconstruction_phrase(lmot:list[str]):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ reconstruction_phrase(['La', 'mission', '47290', 'progresse', '!'])
    'La mission 47290 progresse !'

    """
    res=lmot[0]
    for mot in lmot[1:]:
        res+=' '+mot
    return res

def affichage_message(message:str):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    print(message)
    
def chiffrement(chaine:str,entier:int)->str:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ chiffrement("La mission 47290 progresse !",2)
    'La onmissi 63810 seprogres !'

    """
    list_mot=phrase_en_liste(chaine)
    return reconstruction_phrase(chiffrement_list(list_mot,entier))

def dechiffrement(chaine:str,entier:int)->str:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ dechiffrement('La onmissi 63810 seprogres !',2)
    "La mission 47290 progresse !"
    """
    lres=[]
    list_mot=phrase_en_liste(chaine)
    for mot in list_mot:
        if mot.isdigit():
            lres.append(chiffrement_nombre(mot))
        else:
            lres.append(dechiffrement_mot(mot,entier))
    return reconstruction_phrase(lres)
from random import randint   
def main():
     """ 

     Précondition : 
     Exemple(s) :
     $$$ 
     """
     phrase=saisir()
     entier =randint(2,5)
     phrase_chiffre=chiffrement(phrase,entier)
     affichage_message(phrase_chiffre)
     phrase_dechiffre=dechiffrement(phrase_chiffre,entier)
     affichage_message(phrase_dechiffre)

#Compréhension de code
     
     
# (a) n = [ 1 , 2 ]
# n = n + [3] ∗ 2
# n==[1,2,3,3]
# type(n)== list
# (b) n = "2"
# n = int ( n ) ∗ int ( n ) + f l o a t ( n )
# n==6.0
# type(n)== float
# (c) n = not 0 or 5
# n==True
# type(n)== bool
# (d) u = 0
# v = 1
# w = 2
# n = u != 0 and v // u == w // v
# n==False
# type(n)== bool
# (e) def f ( x ) :
#         if x < 5:
#         qte = 3
#         e l i f x < 10:
#         qte = 2
#         e l i f x < 15:
#         qte = 1
#         else :
#         qte = 0
#         x = x + qte
#     return x
# n=f ( 6 )
# x=8

# def mystere ( a , b ) :
#     c = 0
#     fo r d in a :
#     i f d % b == 0 :
#     c = c + 1
# return c
#>> mystere([3,4,5,6],3)
# 2
# Autre exercice
# 1. n=121231446673253135466736253
# print(n % 7 <= 6)
# True
# 2. print("999" == 3 * "9")
# True
# 3. print("5", '+', "7")
# '5 + 7'
# 4. print(-11---11)
# -22
# 5. x = 1
# y = 2
# z = y
# y = x
# x = z
# print(x, y, z)
# 2 1 2
# 6. z = 0
# print(z < 0 or z != 1)
# True
# 7.print(len("Info") >= len("Math" - "Chimie"))
# typeError:Impossible de faire la difference entre str
# 8. u = 13 > 14
# print(u or not u)
# True
# 9. test = 0
# if test >= 0:
#   test = test - 2
# if test < 0:
#   test = test + 3
# print(test)
# 1
# 10. a = 2
# b = 2
# print((a+b)**2)
# 16
# Autre exercice
# 1. print("9 == 9")
# 9 == 9
# 2. nb3 == 33
# print(nb3)
#nameError: nb3 n'est pas definie
# 3. print("12" == " 12")
# False
# 4. print(6 + -7)
# -1
# 5. print(type("2"))
# str
# 6. print("4" * 2)
# 44
# 7. a = 2
# b = 8
# a = b
# b = b + 1
# print(a)
# 8
# 8. print("Bonjour !\nComment allez-vous ?")
# Bonjour !
# Comment allez-vous ?
# 9. print(len(""))
# 0
# 10. print(11 // 2)
# 5
# Autre exercice
# 1.print(5//2*2)
# 1
# 2. a = "1"
# print(a*3)
# 111
# 3. print("5' + '7")
# 5'+'7
# 4. print(11--11) 
# 22
# 5. x = 1
# y = x
# y = y + 1
# print(x)
# 1
# 6. print(len("PV") > 2)
# False
# 7. z = 0
# print(z > 0 and z != 1)
# False
# 8. u = 13
# print(u = 0 or u = 1)
# SyntaxeInvalide: = c'est l'affectation pas comparaison
# 9. test = 0
# if test >= 0:
#   test = test - 2
# elif test < 0:
#   test = test + 3
# print(test)
# -2
# 10. a = 1
# b = 3
# print((a+b)**2 == a**2 + 2ab + b**2)
# nameError: python ne connait pas ab

if __name__ == '__main__':
    main()