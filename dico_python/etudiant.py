from statistics import mean


def dico_moy(dico: dict)->dict:
    resdico={}
    for key,value in dico.items():
        resdico[key]=mean(value)
    return resdico

def first_student(dico: dict)->tuple[str,float]:
   maxi=max(dico.values())
   for key,value in dico.items():
       if value==maxi:
           return key,value
   return "No match",0

def rang(dico: dict)->list[tuple[str,float]]:
    moy_dico=dico_moy(dico)
    liste=[]
    for i in range(len(moy_dico)):
        liste.append(first_student(moy_dico))
        key=liste[i][0]
        del moy_dico[key]
    return liste

def main(dico: dict):
    moy_dico=dico_moy(dico)
    first=first_student(moy_dico)
    liste=rang(dico)
    print(f'le premier est {first[0]} avec une moyenne: {first[1]}/20')
    print(f'liste complete: \n')
    i=1
    for etu in liste :
        if i==1:
            print(f"{i}er(ere): {etu[0]}\t--\t{etu[1]}")
        else:
            print(f"{i}eme: {etu[0]}\t--\t{etu[1]}")
        i+=1

