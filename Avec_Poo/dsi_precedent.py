
class Poly:
    """ Une classe pour manipuler les polynomes et implantant l'algorithme de Karatsuba.
    $$$ p1 = Poly({0: 3, 1: 2, 3: 1})
    $$$ p1.coeffs
    {0: 3, 1: 2, 3: 1}
    $$$ repr(p1)
    'Poly({0: 3, 1: 2, 3: 1})'
    $$$ p1.degre()
    3
    $$$ p2 = Poly({2: 1, 1: -2, 0: 1})
    $$$ p1 == p2
    False
    $$$ p1 + p2
    Poly({3: 1, 2: 1, 0: 4})
    $$$ nul = Poly({})
    $$$ p1 + nul == p1
    True
    $$$ nul.degre()
    -1
    """
    def __init__(self, coeffs: dict={}):
        self.coeffs = coeffs
    def __repr__(self):
        return f"Poly({self.coeffs})"
    def degre(self) -> int:
        """ 

        Précondition : 
        Exemple(s) :
        $$$ p1=Poly( {3: 3, 6: 2})
        $$$ p1.degre()
        6
        """
        
        if len(self.coeffs) ==0:
            return -1
        return max(list(self.coeffs.keys()))
    def __getitem__(self, n: int) -> int:
        """ Renvoie un coefficient.
            $$$ P = Poly({1: 3, 0: -1})
            $$$ P[1]
            3
            $$$ P[2]
            0
            $$$ P[0]
            -1 """
        return self.coeffs.get(n, 0)
    
    def __setitem__(self, n: int, value: int):
        """ Affecte un coefficient.
        $$$ P = Poly({2: -1, 1: 7, 0: 6})
        $$$ P[2]=3
        $$$ P
        Poly({2: 3, 1: 7, 0: 6}) """
        if value == 0:
            if n in self.coeffs:
                del self.coeffs[n]
            else:
                self.coeffs[n] = value
    def shift(self,n:int):
        """ à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ p1=Poly( {3: 3, 6: 2})
        $$$ p1.shift(4)
        Poly({7: 3, 10: 2})
        """
        dic={}
        for key,value in self.coeffs.items():
            dic[key+n]=value
        return Poly(dic)

    def split(self,n:int):
        """ 

        Précondition : 
        Exemple(s) :
        $$$ p=Poly( {0:2,1:7,3: 3, 6: 2})
        $$$ p.split(3)
        (Poly({0: 3, 3: 2}),Poly({0: 2, 1: 7}))
        
        """
        q={}
        r={}
        for key,value in self.coeffs.items():
            if key>=n:
                q[key-n]=value
            else:
                r[key]=value
        return (Poly(q),Poly(r))

    def __mul__(self, other):
        """ Multiplie deux polynomes en utilisant l'algorithme de Karatsuba.
        $$$ P = Poly({0: 2, 1: 3, 2: 2, 3: 1})
        $$$ Q = Poly({1: 1, 2: -2, 3: 1})
        $$$ P*Q
        Poly({1: 2, 2: -1, 3: -2, 6: 1})
        """
        N=max(self.degre(),other.degre())
        if N <=1:
            return Poly()

                
    
        

## DSI 2024

def bezout(a: int, b: int) -> tuple[int, int]:
    if b == 0:
        res = (1, 0)
    else:
        q = a // b
        (u, v) = bezout(b, a % b)
        res = (v, u - q * v)
    return res

CHIFFRES = "0123456789ABCDEF"

def representation_hexadecimale(entier: int):
    """ 
    Précondition : 
    Exemple(s) :
    $$$ representation_hexadecimale(123)
    '7B'
    """
    if entier<=16:
        return CHIFFRES[entier]
    else:
        return  representation_hexadecimale(entier//16)+str(representation_hexadecimale(entier%16))
def nb_occurrences (chaine:str)->dict:
    """ 
    Précondition : 
    Exemple(s) :
    $$$ nb_occurrences("ROIBABAR")
    {'R': 2, 'O': 1, 'I': 1, 'B': 2, 'A': 2}
    """
    dic={}
    for i in range(len(chaine)):
        prec=chaine[i]
        if not prec in dic.keys():
            val=1
            for carac in chaine[i+1:]:
                if prec==carac:
                    val+=1
            dic[prec]=val    
    return dic

def indice_occurrence(chaine:str)->dict:
    """ 
    Précondition : 
    Exemple(s) :
    $$$ indice_occurrence("ROIBABAR")
    {'R': 0, 'O': 1, 'I': 2, 'B': 3, 'A': 4}
    """
    dic={}
    for i in range(len(chaine)):
        if not chaine[i] in dic.keys():
            dic[chaine[i]]=i
    return dic

def  premier_parmi(caracteres:set(),dico:dict[str,int])->str:
    """ 

    Précondition : 
    Exemple(s) :
    $$$ premier_parmi({'R', 'B', 'A'}, {'R': 0, 'O': 1, 'I': 2, 'B': 3, 'A': 4})
    'R'
    """
    min_indice=min(dico.values())
    for key,value in dico.items():
        if value==min_indice and key in caracteres:
            return key
        
def inverse_dico(dico:dict)->dict:
    """

    Précondition : 
    Exemple(s) :
    $$$ inverse_dico({'R': 2, 'O': 1, 'I': 1, 'B': 2, 'A': 2})
    {2: {'R', 'A', 'B'}, 1: {'O', 'I'}} 
    """
    nouveau = {}
    for cle, val in dico.items():
        if val not in nouveau:
            nouveau[val] = set()
        nouveau[val].add(cle)
    return nouveau
        
class Matrice:
    """
    $$$ m1 = Matrice(2, 3, {(0,1): 1.0, (0, 2): 3.0, (1, 0): 2.0})
    $$$ m1.nb_lignes
    2
    $$$ m1.nb_colonnes
    3
    $$$ m1.coefficients
    {(0,1): 1.0, (0, 2): 3.0, (1, 0): 2.0}
    $$$ repr(m1)
    'Matrice(2, 3, {(0,1): 1.0, (0, 2): 3.0, (1, 0): 2.0})'
    $$$ m2 = Matrice(2, 3, {(0,1): -1.0, (1, 0): 4.0, (1, 1): 3.0})
    $$$ m1 == m2
    False
    $$$ m1 + m2
    Matrice(2, 3, {(0, 2): 3.0, (1, 0): 6.0, (1, 1): 3.0})
    $$$ m1.ligne(0)
    [0.0, 1.0, 3.0]
    $$$ m1.ligne(1)
    [2.0, 0.0, 0.0]
    """
    def __int__(self,nb_lignes:int, nb_colonnes:int,coefficients:dict()):
        self.nb_lignes=nb_lignes
        self.nb_colonnes=nb_colonnes
        self.coefficients=coefficients
    def __repr__(self):
        return f'Matrice({self.nb_lignes},{self.nb_colonnes},{self.coefficients})'
    
    def __eq__(self,other):
        if isinstance(other,Matrice):
            if self.nb_lignes==other.nb_lignes and self.nb_colonnes==other.nb_colonnes:
              return self.coefficients==other.coefficients
        return False
    def __add__(self,other):
        if isinstance(other,Matrice):
            if self.nb_lignes==other.nb_lignes:
                lvaleur1=[value for value in self.coefficients.values() ]
                lvaleur2=[]
                
                    
                for key in other.coefficients.values():
                    lvaleur2.append(key)
                result={}
                lkey=[]
                for value in self.coefficients.keys():
                    lkey.append(value)
                for i in range(len(lkey)):
                    s=lvalue1[i]+lvalue2[i]
                    if s!=0:
                        result[lkey1[i]]=s
        return result

    def ligne(self,ligne:int)->list[float]:
        """ à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ m1 = Matrice(2, 3, {(0,1): 1.0, (0, 2): 3.0, (1, 0): 2.0})
        $$$ m1.ligne(0)
        [0.0, 1.0, 3.0]
        """
        
        lresult=[]
        for key,value in self.coefficients.items():
            if value[0]==ligne:
                lresult.append(key)
        return lresult
# DSI MIAge
class Chrono:
    """
    $$$ t = Chrono(12, 21, 14)
    $$$ t.heures = 12
    $$$ t.minutes = 21
    $$$ t.secondes = 14
    $$$ repr(t)
    'Chrono(12, 21, 14)'
    $$$ str(t)
    '12h21m14s'
    $$$ t.en_secondes()
    44474
    $$$ t == Chrono(12, 21, 14)
    True
    $$$ t == Chrono(13, 21, 14)
    False
    $$$ Chrono(13, 22, 15) - Chrono(12, 21, 14)
    3661
    """
    def __int__(self,heures:int ,minutes:int, secondes:int)->int:
        self.heures=heures
        self.minutes=minutes
        self.secondes=secondes

    def __repr__(self):
        return f"Chrono({self.heures},{self.minutes},{self.secondes})"
    def __str__(self):
        return f"{self.heures}h{self.minutes}m{self.secondes}s"
    def en_secondes(self):
        return self.heures*3600+self.minutes*60+self.secondes
    def __eq__(self,other):
        if isinstance(other,Chrono):
            if self.heures==other.heures:
                if self.minutes==other.minutes:
                    return self.secondes==other.secondes
        return False
    def __sub__(self,other):
        if isinstance(other,Chrono):
            return self.en_secondes()-other.en_secondes()



def total_command(command: dict, livreur: dict) -> float:
        somme = 0
        for produit in command:
            if produit in livreur:
                somme += command[produit] * livreur[produit]
        return somme

def peut_etre_honoree(command: dict, livreur: dict) -> bool:
    for produit in command:
        if not produit in livreur:
            return False
    return True
def propositions_prix (command: dict, dicolivreur: dict) -> dict:
    result={}
    for livreur in dicolivreur:
        if peut_etre_honoree(command,dicolivreur[livreur]):
            result[livreur] = total_command(command,dicolivreur[livreur])
    return result
reine_morgane = {'servomoteur': 9.00, 'peinture': 62.00}
aladin = {'servomoteur': 6.50, 'tête chauffante': 8.20}
andromaque = {'servomoteur': 8.90, 'peinture': 61.99, "tête chauffante": 11.90}

print(propositions_prix({'servomoteur': 10, 'tête chauffante': 2},{ "Reine Morgane": reine_morgane, "Aladin": aladin,"Andromaque": andromaque}))



    
        
      
    
        
        
        
        
    
    
    
        
