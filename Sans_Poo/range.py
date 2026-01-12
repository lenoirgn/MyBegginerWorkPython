# Compléter ici (noms, groupe, contenu fichier, date)
#Mamadou Radjaye sow MI23 Traite de range.py Le 22/10/2025
#
#
#
# Ne pas supprimer cette ligne. <trace>range.py</trace>

def compte_motif(motif, chaine):
    """ renvoie le nombre d’occurrences de motif dans texte

    Précondition : 
    Exemple(s) :
    $$$ compte_motif('la', 'la vitre est sale, lave-la vite')
    3
    $$$ compte_motif('te', 'la vitre est sale, lave-la vite')
    1
    $$$ compte_motif('l', 'la vitre est sale, lave-la vite')
    4
    $$$ compte_motif('politesse', 'la vitre est sale, lave-la vite')
    0
    """
    compt=0
    for i in range(0,len(chaine)):
        if motif ==chaine[i:i+len(motif)]:
            compt+=1
    return compt
       

def indice_maximum(lentier=[int]):
    """renvoie l’indice du maximum d’une liste d’entier

    Précondition : 
    Exemple(s) :
    $$$ indice_maximum([-12, 3, 0])
    1
    $$$ indice_maximum([12, 3, 0])
    0
    """
    maxi=0
    max_indices=0
    for i in range(len(lentier)):
        if lentier[i]>maxi:
            max_indices=i
            maxi =lentier[i]
        
    return max_indices
    


def moyenne_ponderee(lnotes, lcoeff):
    """ envoie la moyenne pondérée des notes par ces coefficients.

    Précondition : 
    Exemple(s) :
    $$$ moyenne_ponderee([5,5],[2,1])
    5
    """
    lg=len(lnotes)
    moyenne=0
    for i in range(lg):
        moyenne+=(lnotes[i]*lcoeff[i])/sum(lcoeff)
    return moyenne
 
    

#################
### Addition binaire
#################
def addition_digit(digit1:str, digit2:str, retenue:str)->tuple[str, str]:
    """ renvoie le couple (retenue, unité) résultant de leur addition

    Précondition : 
    Exemple(s) :
    $$$ addition_digit('0', '1', '0')
    ('0','1')
    """
    somme=int(digit1)+int(digit2)+int(retenue)
    if somme==0:
       retenue=0
       unite=0
    elif somme==1:
        retenue=0
        unite=1
    elif somme==2:
        retenue=1
        unite=0
    else:
        retenue=1
        unite=1
    return (str(retenue),str(unite))
    
def inverser(binaire1:str)->str:
    """ renvoie l'inverse

    Précondition : 
    Exemple(s) :
    $$$ inverser('inverser')
    'resrevni'
    """
    return binaire1[::-1]
    
def addition(binaire1:str,binaire2:str)->str:
    """ renvoie la somme binair

    Précondition : 
    Exemple(s) :
    $$$ addition('0011', '1110')
    '10001'
    $$$ addition('01', '01')
    '010'
    """
    retenue=0
    resultat=''
    binaire1=inverser(binaire1)
    binaire2=inverser(binaire2)
    
    for i in range(len(binaire1)):
        retenue,unite=addition_digit((binaire1[i]),(binaire2[i]),str(retenue))
        resultat=unite+resultat
    resultat=retenue+resultat
    
    return resultat
             
    

#################
## Plutôt parcours en parallèle ou plutôt for imbriqués ?
#################

def determine(lmots:list[str], ldeterminants:list[str])->list[str]:
    """ renvoie les listes des compositions possibles, séparées par une espac

    Précondition : 
    Exemple(s) :
    $$$ determine(['mot', 'chat', 'verre'], ['le', 'un'])
    ['le mot', 'un mot', 'le chat', 'un chat', 'le verre', 'un verre']
    $$$ determine(['mot'], ['le', 'un'])
    ['le mot', 'un mot']
    $$$ determine(['mot'], ['le'])
    ['le mot']
    """
    lres=[]
    ESP=' '
    for mot in lmots:
        for determinants in ldeterminants:
            lres.append(determinants+ESP+mot)
    return lres
            
def supprimer(chaine:str,carac:str)->str:
    """ Renvoie sans carac
    Précondition : 
    Exemple(s) :
    $$$ supprimer('moi','o')
    'mi'
    $$$ supprimer('moi','p')
    'moi'
    """
    reschaine=''
    for car in chaine:
        if carac != car:
            reschaine+=car
    return reschaine
            
    

def supprime(lchaines:list[str], carac:str)->list[str]:
    """ renvoie une nouvelle liste dans laquelle les occurrences du caractère ont été supprimées des chaîne

    Précondition : 
    Exemple(s) :
    $$$ supprime(['le', 'chat', 'miaule'], 'a')
    ['le', 'cht', 'miule']
    """
    lres=[]
    for chaine in lchaines:
        if carac in chaine:
            res=supprimer(chaine,carac)
            lres.append(res)
        else:
            lres.append(chaine)
            
    return lres
        
    
    

def filtre(lcouples:list[int], lvrai:bool):
    """ Renvoie une nouvelle liste ne gardant que les entiers correspondant à un booléen valant True.

    Précondition : 
    Exemple(s) :
    $$$ filtre([1, 2, 4], [True, False, True])
    [1, 4]
    $$$ filtre([1, 2, 4], [True, True, True])
    [1, 2, 4]
    $$$ filtre([1, 2, 4], [False, False, False])
    []
    $$$ filtre([1], [True])
    [1]
    """
    lres=[]
    
    for i in range(len(lvrai)):
        if lvrai[i]:
            lres.append(lcouples[i])
    return lres
    

