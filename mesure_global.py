# MI Prog - TP manipulations - 2324 
# M. Nebut
# sept 23 - révisé sept 24

# Ne pas supprimer cette ligne. <trace>mesure_global.py</trace>

YARD_2_CM = 91.44 #1 yard vaut 91,44 cm
MILE_2_KM = 1.609 #1 mile vaut 1,609 km

import math

def imperial2metrique(yard : int, mile : int) -> int :
    """Renvoie la partie entière de la conversion en mètre d'une
    distance exprimée en yards et en miles.

    Précondition : yard et mile >= 0
    Exemple(s) :
    $$$ imperial2metrique(0, 0)
    0
    $$$ imperial2metrique(1, 1)
    1609
    $$$ imperial2metrique(2, 1)
    1610
    """
    yard_cm = yard * YARD_2_CM
    mile_km = mile * MILE_2_KM
    return math.floor(yard_cm * 0.01 + mile_km * 1000)
