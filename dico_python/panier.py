def update(liste:list[dict],other:list[dict]) -> list[dict[str,str]]:
    for modif in other:
        for produit in liste:
            if produit["nom"] == modif["nom"]:
                produit["quantite"] -= modif["quantite"]
    return liste

def totaux_elet(liste:list[dict]) -> list[dict]:
    lres=[]
    for elem in liste:
        resdic = {}
        resdic[elem['nom']]=elem['prix']*elem['quantite']
        lres.append(resdic)
    return lres

def totaux(liste:list[dict]) -> float:
    res=0.
    for elem in liste:
        res+=elem['quantite']*elem['prix']
    return res



