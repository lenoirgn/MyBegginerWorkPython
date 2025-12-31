def est_minuscule_latine(carac:str)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ est_minuscule_latine('f')
    True
    $$$ est_minuscule_latine('F')
    False
    $$$ est_minuscule_latine('8')
    False
    $$$ est_minuscule_latine('!')
    False
    """
    return carac.islower()

def ne_contient_que_minuscule(chaine:str)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ ne_contient_que_minuscule("bonjour")
    True
    $$$ ne_contient_que_minuscule("bonjouR")
    False
    $$$ ne_contient_que_minuscule("Bonjour")
    False
    """
    for carac in chaine:
        if not est_minuscule_latine(carac):
            return False
    return True

POINTS_LETTRES=[('aeilnorstu',1),('dgm',2),('bcp',3),('fhv',4),('jq',8),('kwxyz',10)]
 
def mot_selectionne(liste:list[str])->list[str]:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ mot_selectionne(['sow', 'mamaDou','radjaye','a'])
    ['sow','radjaye']
    """
    lres=[]
    for elet in liste:
        if len(elet)>1 and ne_contient_que_minuscule(elet):
            lres.append(elet)
    return lres
def est_dans_lettres(carac:str,couple:tuple[str,int])->bool:
    """
    Précondition : 
    Exemple(s) :
    $$$ est_dans_lettres('s',('sow',3))
    True
    $$$ est_dans_lettres('y',('sow',3))
    False
    """
    return carac in couple[0]
def indice_association(carac:str,liste:list[tuple[str,int]])->int:
    """

    Précondition : 
    Exemple(s) :
    $$$ indice_association('a',POINTS_LETTRES)
    0
    $$$ indice_association('z',POINTS_LETTRES)
    5
    """
    for i in range(len(liste)):
        if est_dans_lettres(carac,liste[i]):
            return i
        
def score_mot(mot:str)->int:
    """ 
    Précondition : 
    Exemple(s) :
    $$$ score_mot('oui')
    3
    $$$ score_mot('whisky')
    36
    """
    res=0
    for carac in mot:
        indice=indice_association(carac,POINTS_LETTRES)
        res+=POINTS_LETTRES[indice][1]
    return res

def plateau_vide(entier:int)->list[list[str]]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ plateau_vide(3)
    [['','',''],['','',''],['','','']]
    """
    ligne=['']*entier
    grille=[]
    for i in range(entier):
        grille.append(ligne.copy())
    return grille

plateau=[['n','',''],['o','u',''],['n','','']]

def peut_placer_lettre(carac:str,plateau:list[list[str]],i:str,j:str)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ peut_placer_lettre('i',plateau,1,2)
    True
    $$$ peut_placer_lettre('o',plateau,1,0)
    True
    $$$ peut_placer_lettre('i',plateau,2025,42)
    False
    $$$ peut_placer_lettre('i',plateau,1,0)
    False
    """
    return (i<len(plateau) and  j<len(plateau)) and (plateau[i][j]=='' or plateau[i][j]==carac)
    
def peut_placer_mot_horizontale(mot:str,plateau:list[list[str]],indligne:str,indcol:str)->bool:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ peut_placer_mot_horizontale('oui',plateau,1,0)
    True
    $$$ peut_placer_mot_horizontale('yes',plateau,1,0)
    False
    $$$ peut_placer_mot_horizontale('ouillesadepasse',plateau,1,0)
    False
    """
    for i in range(len(mot)):
        if not peut_placer_lettre(mot[i],plateau,indligne,indcol+i):
            return False
    return True

plateau1=[['','h','i'],['o','u',''],['','n','']]

def debut_mot_horizontal(plateau:list[list[str]],indligne:str,indcol:str)->int:
    """
    Précondition : 
    Exemple(s) :
    $$$ debut_mot_horizontal(plateau1,0,2)
    1
    $$$ debut_mot_horizontal(plateau1,1,1)
    0
    """
    
    while indcol >=0 and plateau[indligne][indcol-1]!='':
        indcol-=1
    return indcol
    
        
        
        
    

        
                
    
            
            
    
    