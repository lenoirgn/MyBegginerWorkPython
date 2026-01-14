from matrice import *
def test_dimensionTrue():
    A = [[1,2],[3,4]]
    B = [[5,6],[7,8]]
    assert  dimension_egale(A,B) == True
def test_dimensionFalse():
    A = [[1,2],[3,4],[5,6]]
    B = [[5,6],[7,8]]
    assert  dimension_egale(A,B) == False

def test_sommeAdd():
    A = [[1,2],[3,4]]
    B = [[5,6],[7,8]]
    assert somme(A,B,1) == [[6, 8], [10, 12]]

def test_sommeDiff():
    A = [[1,2,5],[3,4,5]]
    B = [[5,6,4],[7,8,6]]
    assert somme(A,B,2) == [[-4, -4, 1], [-4, -4, -1]]

def test_sont_egaleTrue():
    A = [[1,2,3],[4,5,6]]
    B = [[5,6],[8,9],[7,9]]
    assert sont_egale(A,B)==True
def test_sont_egaleFalse():
    A = [[1,2,3],[4,5,6]]
    B = [[5,6],[8,9]]
    assert sont_egale(A,B)==False
def test_somme_produit():
     A=[1,2,3]
     B=[4,5,6]
     assert somme_produit(A,B)==32

def test_produit1():
    A=[[1,2,3],[4,5,6]]
    B=[[5,6],[8,9],[7,9]]
    assert produit(A,B)==[[42, 51], [102, 123]]

def test_produit2():
    A=[[1,2,3,7],[4,5,6,4]]
    B=[[5,6],[8,9],[7,9],[1,1]]
    assert produit(A,B)==[[49, 58], [106, 127]]

def test_produit3():
    A=[[1,2,3],[4,5,6]]
    B=[[5,6,4],[8,9,2],[7,9,1]]
    assert produit(A,B)==[[42, 51, 11], [102, 123, 32]]


