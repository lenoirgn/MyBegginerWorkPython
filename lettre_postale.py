def tarif_lettre_verte(poids:float)->float:
    """ Renvoie le tarif a payer

    Précondition : poids<=250g
    Exemple(s) :
    $$$ 
    """
    if poids<=20:
        tarif=1.16
    elif poids<=100:
        tarif=2.32
    elif poids<=250:
        tarif=4.00
    return tarif
def tarif_envoi_multiple_vertes (liste:list[int])->float:
    """ Renvoie le tarif a payer

    Précondition : 
    Exemple(s) :
    $$$ tarif_envoi_multiple_vertes([11, 8, 34])
    4.64
    """
    tarif=0
    tarif_elm=0
    for valeur in liste:
        tarif_elm=tarif_lettre_verte(valeur)
        tarif+=tarif_elm
        
    return tarif
def timbre_suffisant_lettre_verte(poid:float,valeur_timbre:float)->bool:
    """ renvoie True ssi cette valeur est suffisante pour l’envoi de la lettre

    Précondition : 
    Exemple(s) :
    $$$ timbre_suffisant_lettre_verte(10,0.5)
    False
    $$$ timbre_suffisant_lettre_verte(10,3)
    True
    """
    return valeur_timbre>=tarif_lettre_verte(poid)
def a_temps(type_lettre:str,delai:int)-> bool:
    """ envoie True ssi la lettre a été distribuée en respectant les délais postaux

    Précondition : 
    Exemple(s) :
    $$$ a_temps('prioritaire',3)
    False
    $$$ a_temps('verte',3)
    True
    $$$ a_temps('suivie',1)
    True
    """
    return (type_lettre=='prioritaire' and delai<=1) or (type_lettre=='suivie' and delai<=2) or (type_lettre=='verte')
def delais_courts(lentiers:list[int])->list[int]:
    """ envoie une nouvelle liste qui contient les éléments de la liste passée en paramètre, dans le même
    ordre, en ayant supprimé les valeurs strictement supérieures à 6.

    Précondition : 
    Exemple(s) :
    $$$ delais_courts([1,2,3,7,9])
    [1,2,3]
    $$$ delais_courts([6,1,2,3,7,9])
    [6,1,2,3]
    """
    lres=[]
    for entier in lentiers:
        if not entier>6:
            lres.append(entier)
    return lres
def delai_minimal(lentiers:list[int])->int:
    """ renvoie le délai minimal

    Précondition : 
    Exemple(s) :
    $$$ delai_minimal([6,1,2,3,7,9])
    1
    $$$ delai_minimal([1,2,1,3,1,9])
    1
    """
    mini=lentiers[0]
    for entier in lentiers[1:]:
        if mini >entier:
            mini=entier
    return mini
            
    
def infos_compte (cle:str, NCN:str)->str :
    """ Renvoie l'info du compte

    Précondition : 
    Exemple(s) :
    $$$ infos_compte('14', '30001019010000Z67067032')
    'FR1430001019010000Z67067032'
    """
    return 'FR'+cle+NCN
def nb_similitudes(iban1:str, iban2:str)->int:
    """ Renvoie le nombre de caractères identiques à la même position dans les deux NCN

    Précondition : 
    Exemple(s) :
    $$$ nb_similitudes('FR1430001019010000Z67067032','FR1420041010050500013L02606')
    9
    """
    compt=0
    for i in range(23):
        if iban1[4+i]==iban2[4+i]:
            compt+=1
    return compt
def liste_iban(iban:str):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ liste_iban('FR1430001019010000Z67067032:FR1420041010050500013L02606')
    ['FR1430001019010000Z67067032', 'FR1420041010050500013L02606']
    """
    iban1=iban[0:27]
    iban2=iban[28:]
    lres=[]
    lres.append(iban1)
    lres.append(iban2)
    return lres
    
def nb_max_0(iban:str) ->str:
    """ Renvoie le nombre max de 0 consecutif

    Précondition : 
    Exemple(s) :
    $$$ nb_max_0('FR1430001019010000Z67067032')
    4
    """
    maxi=1
    comp=0
    for carac in iban:
        if carac=='0':
            comp+=1
            if maxi<comp:
                maxi=comp
        else:
            comp=0
    return maxi
       
        
        
    