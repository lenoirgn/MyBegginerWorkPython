import os.path



def fusion_liste(liste0:list[int],liste1:list[int])->list[int]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ fusion_liste([1, 4, 6, 12],[1 ,2 ,3 ,6 ,20 ,22])
    [1 ,2 ,3 ,4,  6, 12, 20, 22]
    $$$ fusion_liste([1, 4, 6, 12,56,89],[1 ,2 ,3 ,6 ,20 ,22])
    [1 ,2 ,3 ,4,  6, 12, 20, 22,56,89]
    $$$ fusion_liste([2, 4, 6, 12,56,89],[1 ,20 ,22])
    [1 ,2  ,4,  6, 12, 20, 22,56,89]
    $$$ fusion_liste([2, 4, 6, 12,56,89],[1 ,22,105])
    [1 ,2  ,4,  6, 12,  22,56,89,105]
    $$$ fusion_liste([1 ,22,105],[2, 4, 6, 12,56,89])
    [1 ,2  ,4,  6, 12,  22,56,89,105]
    """
    i=0
    j=0
    lres=[]
    while i<len(liste0) and j< len(liste1):
        if liste0[i]==liste1[j]:
            lres.append(liste0[i])
            i+=1
            j+=1
        elif liste0[i]>liste1[j]:
            lres.append(liste1[j])
            j+=1
        elif liste0[i]<liste1[j]:
            lres.append(liste0[i])
            i+=1
    if i==len(liste0):
        for elt in liste1[j:]:
            lres.append(elt)
    else:
        for elt in liste0[i:]:
            lres.append(elt)
 
    return lres

def fusion_fichier_readlines(fichier1:str,fichier2:str):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    with open (fichier1,'r') as f1:
        liste1=[]
        for elt in f1.readlines():
            liste1.append(int(elt.strip()))
        
    with open (fichier2,'r') as f2:
        liste2=[]
        for elt in f2.readlines():
            liste2.append(int(elt.strip()))
      
    liste3=fusion_liste(liste1,liste2)
   
    with open ('fichier3.txt','w') as f3:
        for entier in liste3:
            f3.write(str(entier).strip() +'\n')
        
def fusion_fichier_readline(fichier1:str,fichier2:str):
    """ 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    with open (fichier1,'r') as f1,open (fichier2,'r') as f2 ,open ('fichier3.txt','w') as f3:
         entier1=f1.readline()
         entier2=f2.readline()
         while entier1!='' and entier2!='' :
             if int(entier1.strip())==int(entier2.strip()):
                 f3.write(str(entier1).strip() +'\n')
                 entier1=f1.readline()
                 entier2=f2.readline()
             elif int(entier1.strip())<int(entier2.strip()):
                 f3.write(str(entier1).strip() +'\n')
                 entier1=f1.readline()
             elif int(entier1.strip())>int(entier2.strip()):
                 f3.write(str(entier2).strip() +'\n')
                 entier2=f2.readline()
         while entier1 !='':
             f3.write(entier1.strip() +'\n')
             entier1=f1.readline()
         while entier2 !='':
             f3.write(entier2.strip() +'\n')
             entier2=f2.readline()
            
                 
             
                 
         
    
    