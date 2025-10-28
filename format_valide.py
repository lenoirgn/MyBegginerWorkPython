def est_chiffre_oblique(caractere:str):
    """ 
    Précondition : 
    Exemple(s) :
    $$$ est_chiffre_oblique('2')
    True
    $$$ est_chiffre_oblique('/')
    True
    $$$ est_chiffre_oblique('n')
    False
    """
    return caractere.isdigit() or caractere=='/'
def compte_chiffre_oblique(chaine:str):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ compte_chiffre_oblique('13/10/22')
    8
    $$$ compte_chiffre_oblique('25-12-2022')
    8
    $$$ compte_chiffre_oblique('///0/')
    5
    """
    compt=0
    for carac in chaine:
        if est_chiffre_oblique(carac):
            compt+=1
            
    return compt 
def contient_caracteres_date_v1(chaine:str)->bool:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ contient_caracteres_date_v1('13/10/22')
    True
    $$$ contient_caracteres_date_v1('///0/')
    True
    $$$ contient_caracteres_date_v1('25-12-2022')
    False
    """
    return compte_chiffre_oblique(chaine) == len(chaine)
def contient_caracteres_date_v2(chaine:str)->bool:
    """

    Précondition : 
    Exemple(s) :
    $$$ contient_caracteres_date_v2('13/10/22')
    True
    $$$ contient_caracteres_date_v2('///0/')
    True
    $$$ contient_caracteres_date_v2('25-12-2022')
    False
    """
    vrai=True
    
    for carac in chaine:
        if not est_chiffre_oblique(carac):
            vrai=False
            break
            
    return vrai
       

     
        
            