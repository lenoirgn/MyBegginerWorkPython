from math import sqrt

class Vecteur:
    """ 

    Exemple(s) :
    
    
    """
    
    def __init__(self,dimension:list[float]):
         self.dimension =dimension
        
    def __str__(self):
        """

        Précondition : 
        Exemple(s) :
        $$$ 
        
        """
        return f"{self.dimension}"
    def __repr__(self):
        return f"Vecteur(self.dimension)"
    
    def composante (self, n:int)->float:
        """ Renvoie

        Précondition : n<len(self.dimension)
        Exemple(s) :
        $$$ 
        """
        return self.dimension[n]
    
    def __add__(self,other)->list[float]:
        """ return self+other

        Précondition : len(self.dimension)==len(other.dimension)
        Exemple(s) :
        $$$ v1=Vecteur([2.0,3.4,1.4])
        $$$ v2=Vecteur([6.0,3.0,-2.8])
        $$$ v1+v2
        [8.0,6.4,-1.4]
        """
        if isinstance(other,Vecteur):
            res=[]
            for i in range(len(self.dimension)):
                res.append(self.dimension[i]+other.dimension[i])
            return res
        
    def __sub__(self,other)->list[float]:
        """return self-other

        Précondition : len(self.dimension)==len(other.dimension)
        Exemple(s) :
        $$$ 
        """
        if isinstance(other,Vecteur):
            res=[]
            for i in range(len(self.dimension)):
                res.append(self.dimension[i]-other.dimension[i])
            return res
        
    def __mul__(self,other)->list[float]:
        """return self*other

        Précondition : len(self.dimension)==len(other.dimension)
        Exemple(s) :
        $$$ 
        """
        if isinstance(other,Vecteur):
            res=[]
            for i in range(len(self.dimension)):
                res.append(self.dimension[i]*other.dimension[i])
            return res
                
    def __truediv__(self,other) ->list[float]:
        """return self/other

        Précondition : len(self.dimension)==len(other.dimension)
        Exemple(s) :
        $$$ 
        """
        if isinstance(other,Vecteur):
            res=[]
            for i in range(len(self.dimension)):
                if other.dimension[i]!=0:
                    res.append(self.dimension[i]/other.dimension[i])
                    return res
                else:
                    raise ValueError("impossible de diviser par 0")
                
        
    def __mul__(self,n:float)->list[float]:
        """return self*n

        Précondition : len(self.dimension)==len(other.dimension)
        Exemple(s) :
        $$$ 
        """
        res=[]
        for i in range(len(self.dimension)):
            res.append(self.dimension[i]*n)
        return res
    
    
        
    def __neg__(self) ->list[float]:
        """ return -self

        Précondition : 
        Exemple(s) :
        $$$ 
        """
        res=[]
        for i in range(len(self.dimension)):
            res.append(self.dimension[i]*(-1))
        return res
    
    def __pos__(self) ->list[float]:
        """ 
         return +self
        Précondition : 
        Exemple(s) :
        $$$ 
        """
        res=[]
        for i in range(len(self.dimension)):
            res.append(abs(self.dimension[i]))
        return res
    
    def __eq__(self,other)->bool:
        """ 

        Précondition : len(self.dimension)==len(other.dimension)
        Exemple(s) :
        $$$ 
        """
        if isinstance(other,Vecteur):
            for i in range(len(self.dimension)):
                if self.dimension[i]!=other.dimension[i]:
                    return False 
            return True
        
    def __lt__(self,other)->bool:
        """ 

        Précondition : len(self.dimension)==len(other.dimension)
        Exemple(s) :
        $$$ 
        """
        if isinstance(other,Vecteur):
            for i in range(len(self.dimension)):
                if not self.dimension[i]<other.dimension[i]:
                    return False 
            return True
        
    def __gt__(self,other)->bool:
        """ 

        Précondition : len(self.dimension)==len(other.dimension) 
        Exemple(s) :
        $$$ 
        """
        if isinstance(other,Vecteur):
            for i in range(len(self.dimension)):
                if not self.dimension[i]>other.dimension[i]:
                    return False 
            return True
        
    def __ge__(self,other)->bool:
        """ 

        Précondition : len(self.dimension)==len(other.dimension)
        Exemple(s) :
        $$$ 
        """
        if isinstance(other,Vecteur):
            for i in range(len(self.dimension)):
                if not self.dimension[i]>=other.dimension[i]:
                    return False 
            return True
        
    def __le__(self,other)->bool:
        """ 

        Précondition : len(self.dimension)==len(other.dimension)
        Exemple(s) :
        $$$ 
        """
        if isinstance(other,Vecteur):
            for i in range(len(self.dimension)):
                if not self.dimension[i]<=other.dimension[i]:
                    return False 
            return True
            
    def  __ge__(self,other)->bool:
        """ 

        Précondition : len(self.dimension)==len(other.dimension)
        Exemple(s) :
        $$$ 
        """
        if isinstance(other,Vecteur):
            for i in range(len(self.dimension)):
                if not self.dimension[i]<=other.dimension[i]:
                    return False 
            return True          
    def  __ne__(self,other)->bool:
        """ 

        Précondition : len(self.dimension)==len(other.dimension)
        Exemple(s) :
        $$$ 
        """
        if isinstance(other,Vecteur):
            for i in range(len(self.dimension)):
                if not self.dimension[i]==other.dimension[i]:
                    return False 
            return True          
        
        
    def produit_scalaire (self,other)->float:
         """ 

         Précondition : 
         Exemple(s) :
         $$$ 
         """
         if isinstance(other,Vecteur):
            res=0.0
            for i in range(len(self.dimension)):
                res+=self.dimension[i]*other.dimension[i]
            return res
         
    def module(self) ->list[float]:
        """ 
         return le module
        Précondition : 
        Exemple(s) :
        $$$ 
        """
        res=0.0
        for i in range(len(self.dimension)):
            res+=(self.dimension[i])**2
        return sqrt(res)
    
    def  max(self, liste:list[list[float]])->list[float]:
        """ 

        Précondition : 
        Exemple(s) :
        $$$ 
        """
        res=[]
        for i in range(len(liste)):
            colonne=[]
            for j in range(len(liste)):
                colonne.append(liste[j][i])
            res.append(max(colonne))
        return res

        
        
    