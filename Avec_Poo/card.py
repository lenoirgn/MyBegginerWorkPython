from random import choice
class Card:
    VALUES=["Ace", "2","3","4","5","6","7","8", "9", "10", "Jack", "Knight", "Queen", "King"]
    COLOR=["spade", "heart", "diamond", "club"]
    def __init__(self,value,color):
        assert value in self.VALUES and color in self.COLOR,"Ces valeurs n'existe pas"
        self.value=value
        self.color=color

    def random():
        return Card(choice(Card.VALUES),choice(Card.COLOR))

    def compare(self,other):
        v_index1=Card.VALUES.index(self.value)
        v_index2=Card.VALUES.index(other.value)
        if v_index1!=v_index2:
            return v_index1-v_index2
        else:
            c_index1=Card.COLOR.index(self.color)
            c_index2=Card.COLOR.index(other.color)
            if c_index1!=c_index2:
                return c_index1-c_index2
            else:
                return 0
    def __str__(self):
        return f"La carte :({self.value},{self.color})"
    def __eq__(self,other):
        return Card.compare(self,other)==0
    def __lt__(self,other):
        return Card.compare(self,other)<0
    def __gt__(self,other):
        return Card.compare(self,other)>0
    def diff(self,other):
        return not self==other




