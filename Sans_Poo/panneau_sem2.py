# Compléter ici (noms, groupe, contenu fichier, date)
#Mamadou Radjaye sow, MI23,Mon traite_paaneau_sem2,Le 12/09/2025
#
#
#
# Ne pas supprimer cette ligne. <trace>panneau_sem2.py</trace>

ESP=" "
def panneau(ville:str, nb_rangs:int)->str:
    """ Renvoie un panneau de decoration du nom d'une ville

    Précondition : ville !='' et nb_rangs >0 
    Exemple(s) :
    $$$ 
    """
    haut=nb_rangs*(nb_rangs*'*'+(nb_rangs-1)*'*'+len(ville)*'*'+(nb_rangs-1)*'*'+nb_rangs*'*'+'\n')
    milieu_avant=nb_rangs * (nb_rangs*'*'+ ESP*(nb_rangs-1) + ESP*len(ville) + ESP*(nb_rangs-1) + nb_rangs*'*'+'\n')
    ligne= nb_rangs*'*' + ESP*(nb_rangs-1)+ ville + ESP*(nb_rangs-1) + nb_rangs*'*' +'\n' 
    milieu_apres=  nb_rangs * (nb_rangs*'*' + ESP*(nb_rangs-1) + ESP*len(ville) + ESP*(nb_rangs-1) + nb_rangs*'*'+'\n')      
    bas =  nb_rangs*(nb_rangs*'*'+(nb_rangs-1)*'*'+len(ville)*'*'+(nb_rangs-1)*'*'+nb_rangs*'*'+'\n' )    
     
    return haut + milieu_avant+ligne+ milieu_apres+bas
    