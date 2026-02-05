class Book:
    def __init__(self, title:str,author:str,year:int,disponible:bool):
        self.title = title
        self.author = author
        self.year = year
        self.disponible = disponible
    def __str__(self):
        return f'{self.title} de {self.author} '
    def emprunter(self):
        if self.disponible:
            self.disponible = False
            return True
        return False
    def retourner(self):
        if not self.disponible:
            self.disponible = True
            return True
        raise ValueError("Le livre est déjà disponible")
