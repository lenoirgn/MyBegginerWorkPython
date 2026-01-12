from random import uniform
from math import sqrt
def generer_point (v_max:int):
    """ Renvoie un point du carre

    Précondition :
    Exemple(s) :
    """
    x= uniform(-v_max/2,v_max/2)
    y= uniform(-v_max/2,v_max/2)
    x=round(x,2)
    y=round(y,2)
    return [x,y]
def est_dans_cercle(point:list,rayon:int)->bool:
    """ Renvoie True si le point appartient au point

    Précondition :
    Exemple(s) :
    $$$ est_dans_cercle([-3,3],5)
    True
    $$$ est_dans_cercle([-3,3],2)
    False
    $$$ est_dans_cercle([-3,3],9)
    True
    """
    x=point[0]
    y=point[1]
    distance_OM=sqrt(x**2+y**2)
    return  distance_OM <= rayon

def generer_liste_points(nb_point:int, v_max:int)->list:
    """ Renvoie une liste de triple

    Précondition :
    Exemple(s) :
    $$$ 
    """
    liste=[]
    res=()
    for i in range(nb_point):
     points=generer_point(v_max)
     du_cercle=est_dans_cercle(points,v_max/2)
     x_point=points[0]
     y_point=points[1]
     res_tuple=tuple([x_point,y_point,du_cercle])
     liste.append(res_tuple)
    return liste
def nb_point_cercle (listTriple:list[(int,int,bool)])->int:
    """ Renvoie le nombre de point du cercle

    Précondition :
    Exemple(s) :
    $$$ nb_point_cercle([(2,3,False),(2,3,True),(2,3,False)])
    1
    $$$ nb_point_cercle([(2,3,True),(2,3,True),(2,3,True)])
    3
    $$$ nb_point_cercle([(2,3,False),(2,3,False),(2,3,False)])
    0
    """
    nb_point_duCerxle=0
    for point in listTriple:
       if point[2]==True:
          nb_point_duCerxle+=1
    return nb_point_duCerxle

def calcul_pi (listTriple:list[(int,int,bool)])->float:
    """ Renvoie une valeur approche de pi

    Précondition :
    Exemple(s) :
    $$$ calcul_pi([(2,3,False),(2,3,True),(2,3,False)])
    4*1/3
    $$$ calcul_pi([(2,3,False),(2,3,False),(2,3,False)])
    0
    """
    point_cercle=nb_point_cercle (listTriple)
    point_total=len(listTriple)
    valeur_pi=(4*point_cercle)/point_total
    return valeur_pi
    
   
          


if __name__ == '__main__':
 
	print ("** Estimer pi avec la pluie **")
	rayon=int(input("Donner le rayon du cercle : "))
	nb_point= int(input("Donner le nombre de points à générer : "))
	listpoint=generer_liste_points(nb_point,rayon*2)
	valeur_pi=calcul_pi(listpoint)
	print(f"La valeur de pi est estimée à : {valeur_pi}")
