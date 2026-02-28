from compare import compare
from typing import Callable

def indice(elet: int, liste: list[int], a: int=0, b: int=None, comp: Callable[[int, int], int] = compare) -> int:
    if b is None:
        b=len(liste)-1
    while a < b and comp(elet, liste[a])!=0:
        a += 1
    if liste[a]==elet:
        return a
    else:
        return -1


def indicev2(elet: int, liste: list[int], a: int=0, b: int=None, comp: Callable[[int, int], int] = compare) -> int:
    if b is None:
        b=len(liste)-1
    trouve=False
    while a < b and trouve==False:
