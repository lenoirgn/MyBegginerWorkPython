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
        if len(self.coeffs) ==0:
            return -1
        return list(self.coeffs.keys())[-1]
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

            
        