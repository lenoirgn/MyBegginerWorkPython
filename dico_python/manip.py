dico={'nom':"Alice",'prenom':"Bob",'age':24}

print(dico.keys())
#dict_keys(['nom', 'prenom', 'age'])
print(dico.values())
#dict_values(['Alice', 'Bob', 24])
dico["profession"]="Developpeur Web"
print(dico.keys())
#dict_keys(['nom', 'prenom', 'age', 'profession'])
print(dico.values())
#dict_values(['Alice', 'Bob', 24, 'Developpeur Web'])
dico["nom"]="Sow"
print(dico)
#{'nom': 'Sow', 'prenom': 'Bob', 'age': 24, 'profession': 'Developpeur Web'}
del dico["age"]
print(dico)
#{'nom': 'Sow', 'prenom': 'Bob', 'profession': 'Developpeur Web'}

def value_key(dic:dict)->dict:

    resdict={}
    for key,value in dic.items():
        resdict[value]=key
    return resdict


print(value_key({'nom': 'Sow', 'prenom': 'Bob', 'age': 24, 'profession': 'Developpeur Web'}))
#{'Sow': 'nom', 'Bob': 'prenom', 24: 'age', 'Developpeur Web': 'profession'}
