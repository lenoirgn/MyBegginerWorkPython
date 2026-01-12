def grille_triangle_inf(entier:int)->list[list[str]]:
    """ Retourne une grille triangulaire inférieure de taille `entier`.
    Précondition : entier > 0
    Exemple(s) :
    $$$ grille_triangle_inf(3)
    [['+', '*', '*'], ['+', '+', '*'], ['+', '+', '+']]
    $$$ grille_triangle_inf(4)
    [['+', '*', '*','*'], ['+', '+', '*','*'], ['+', '+', '+','*'],['+', '+', '+','+']]
    """
    grille=[]
    for i in range(entier):
        grille.append([])
        for j in range(i+1):
            grille[i].append('+')
            
        while len(grille[i])<entier:
            grille[i].append('*')
    return grille
def grille_triangle_sup(entier:int)->list[list[str]]:
    """ Retourne une grille triangulaire supérieure de taille `entier`.
    Précondition :entier > 0
    Exemple(s) :
    $$$ grille_triangle_sup(3)
    [['+', '+', '+'], ['*', '+', '+'], ['*', '*', '+']]
    $$$ grille_triangle_sup(4)
    [['+', '+', '+', '+'], ['*', '+', '+', '+'], ['*', '*', '+', '+'],['*','*', '*','+']]
    """
    grille=[]
    for i in range(entier):
        grille.append([])
        for j in range(i):
            grille[i].append('*')
          
        while len(grille[i])<entier:
            grille[i].append('+')
    return grille            
            
def  grille_croix(entier:int)->list[list[str]]:
    """ Retourne une grille carrée de taille impair `entier` avec une croix centrale en '+'.

    Précondition : entier est impaire
    Exemple(s) :
    $$$ grille_croix(3)
    [['*', '+', '*'], ['+', '+', '+'], ['*', '+', '*']]
    $$$ grille_croix(5)
    [['*', '*', '+', '*', '*'], ['*', '*', '+', '*', '*'], ['+', '+', '+', '+', '+'], ['*', '*', '+', '*', '*'], ['*', '*', '+', '*', '*']]
    $$$ grille_croix(7)
    [['*', '*', '*', '+', '*', '*', '*'], ['*', '*', '*', '+', '*', '*', '*'], ['*', '*', '*', '+', '*', '*', '*'], ['+', '+', '+', '+', '+', '+', '+'], ['*', '*', '*', '+', '*', '*', '*'], ['*', '*', '*', '+', '*', '*', '*'], ['*', '*', '*', '+', '*', '*', '*']]

    """
    grille=[]
    centrale=entier//2
    for i in range(entier):
        grille.append([])
        if i !=centrale:
            for j in range(entier):
                if j==centrale:
                    grille[i].append('+')
                else:
                    grille[i].append('*')
                    
        else:
            for j in range(entier):
                grille[i].append('+')
    return grille
                
                
              
                
                
            
        
            
    
    
    
    