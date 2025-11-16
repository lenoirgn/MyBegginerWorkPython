# Compléter ici (noms, groupe, contenu fichier, date)
# Mamadou Radjaye sow MI23 Traite de hexadecimale le 14/11/025
#
#
#
# Ne pas supprimer cette ligne. <trace>hexadecimal.py</trace>
HEXA = '0123456789ABCDEF'
def hexa_decimal(entier:int)->str:
    """ 
    Précondition : 
    Exemple(s) :
    $$$ hexa_decimal(2014)
    '7DE'
    $$$ hexa_decimal(2004)
    '7D4'
    $$$ hexa_decimal(2025)
    '7E9'
    $$$ hexa_decimal(123456789)
    '75BCD15'
    """
    res=''
    while entier//16!=0:
        reste=entier%16
        entier=entier//16
        res+=HEXA[reste]
    res+=HEXA[entier]
    return res[::-1]
        
def decimal_hexa(chaine:str)->int:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ decimal_hexa('10')
    16
    $$$ decimal_hexa('10DE2')
    69090
    $$$ decimal_hexa('10D5E29')
    17653289
    """
    p=0
    indice=-1
    somme=0
    for i in range(len(chaine)):
        while p<len(HEXA)and HEXA[p]!=chaine[indice]:
            p+=1
        if p==0:
            somme+=0
        else:
            somme+=p*(16**i)
        indice-=1
        p=0
        
    return somme 
   
def est_hexa (chaine:str)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ est_hexa('0x54H')
    False
    $$$ est_hexa('0xZ40')
    False
    $$$ est_hexa('-0x3456C40P')
    False
    $$$ est_hexa('0x3456C40')
    True
    $$$ est_hexa('-0x3456C40')
    True
    $$$ est_hexa('+0x3456C40')
    True
    """
    if chaine[0:2]=='0x' :
        for car in chaine[2:]:
            if not car in HEXA:
                return False
        return True
    elif  chaine[0:3]=='-0x' or chaine[0:3]=='+0x':
        for car in chaine[3:]:
            if not car in HEXA:
                return False
        return True
    return False
def binaire_deci(chaine:str):
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ binaire_deci('101')
    5
    $$$ binaire_deci('100')
    4
    $$$ binaire_deci('1111001110')
    974
    """
    somme=0
    p=1
    for elt in chaine:
        somme+=int(elt)*(2**(len(chaine)-p))
        p+=1
    return somme
def hexa_binaire (chaine:str)->str:
    """ 
    Précondition : 
    Exemple(s) :
    $$$ hexa_binaire('1011101')
    '5D'
    $$$ hexa_binaire('10111010011101')
    '2E9D'
    """
    while not len(chaine)%4==0:
        chaine='0'+chaine
    
    res=''   
    temp=''
    
    indice_temp=0
    for i in range((len(chaine)//4)):
        
        limit=4
        while len(temp)<limit:
            temp+=chaine[indice_temp]
            indice_temp+=1
        indice=binaire_deci(temp)
        temp=''
        limit+=4
        res+=HEXA[indice]
    return res
def deci_binaire(entier:int)->str:
     """ 

     Précondition : 
     Exemple(s) :
     $$$ deci_binaire(2)
     '10'
     $$$ deci_binaire(2748)
     '101010111100'
     """
     res=''
     while entier//2!=0:
         res+=str(entier%2)
         entier=entier//2
     res+=str(entier)
     return res[::-1]
         
     
def binaire_hexa(chaine:int):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ binaire_hexa('2E9D')
    '0010111010011101'
    $$$ binaire_hexa('2EF59D')
    '001011101111010110011101'
    """
    res=''
    for car in chaine:
        deci_car=decimal_hexa(car)
        binaire_car=deci_binaire(deci_car)
        while len(binaire_car)<4:
            binaire_car='0'+binaire_car
            
        res+=str(binaire_car)
        
    return res
    
    
    
    
from random import choice

def fonction_genere_hexa(entier:int):
    """ 

    Précondition : 
    Exemple(s) :
    """
    res=''
    while len(res) <entier:
        res+=choice(HEXA)
    return res
def genere_hexa_sans_begaiement(entier):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    res=''
    while len(res) <entier:
        choix=choice(HEXA)
        if res=='' or res[-1]!=choix:
            res+=choix
    return res
    
    