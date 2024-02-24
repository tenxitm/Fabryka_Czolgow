
#Pomoc z wykonywaniem zadan

#Listy obiektow

lst_obiektow = []

class Obiekt:
    def __init__(self,a,b,c) -> None:
        self.zmienna1 = a
        self.zmienna2 = b
        self.zmienna3 = c

    def inf(self):
        print(self.zmienna1)
        print(self.zmienna2)
        print(self.zmienna3)
    
    def zmien(self):
        self.zmienna1 = float(input())
        self.zmienna2 = float(input())
        self.zmienna3 = float(input())

lst_obiektow.append(Obiekt(2,4,6))      #by uzyskac liste obiektow ktorych funkcje mozna
                                        #wywolac trzeba je dodawac w taki sposob
lst_obiektow[0].inf()
lst_obiektow[0].zmien()
lst_obiektow[0].inf()
