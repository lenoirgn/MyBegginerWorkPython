from book import Book
class Biblioteque():
    def __init__(self,nom:int,liste:list[Book]):
        self.nom = nom
        self.liste = liste

    def ajout(self,livre:Book):
        self.liste.append(livre)

    def livre_disponible(self):
        liste=[]
        for livre in self.liste:
            if livre.disponible:
                liste.append(livre)
        return liste
    def rechercher_autor(self,autor:str):
        liste=[]
        for livre in self.liste:
            if livre.autor == autor:
                liste.append(livre)
            return liste

