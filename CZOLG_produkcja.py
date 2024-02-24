class Czolg():
    def __init__(self) -> None:
        self.cena
        self.numer_seryjny
        
    
    def zmien1(self,nowa_cena):
        self.cena = nowa_cena

    def inf1(self):
        print(self.cena)

class Dzialo():
    def __init__(self) -> None:
        self.kaliber = kaliber
    
    def zmien2(self, nowy_kaliber):
        self.kaliber = nowy_kaliber

    def inf2(self):
        print(self.kaliber)

class Element3:
    def __init__(self) -> None:
        self.cecha3 = 1
    
    def zmien3(self):
        self.cecha3 = float(input())

    def inf3(self):
        print(self.cecha3)

class Element4:
    def __init__(self) -> None:
        self.cecha3 = 1
    
    def zmien3(self):
        self.cecha3 = float(input())

    def inf3(self):
        print(self.cecha3)

class Element4:
    def __init__(self) -> None:
        self.cecha3 = 1
    
    def zmien3(self):
        self.cecha3 = float(input())

    def inf3(self):
        print(self.cecha3)


class Calosc():                 #nie moznadziedziczyc wiecej niz jednje classy 
    def __init__(self):         #ale za ro mozna zapisac je jako obiekty
        self.elm1 = Element1()
        self.elm2 = Element2()
        self.elm3 = Element3()
    
    def inf(self):
        self.elm1.inf1()
        self.elm2.inf2()
        self.elm3.inf3()
    
    def zmien(self):
        self.elm1.zmien1()
        self.elm2.zmien2()
        self.elm3.zmien3()
    
x = Calosc()

# x.inf()
# x.zmien()
# x.inf()
