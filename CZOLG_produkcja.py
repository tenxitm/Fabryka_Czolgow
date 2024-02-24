class Czolg():
    def __init__(self,cena,numer_seryjny) -> None:
        self.cena
        self.numer_seryjny
        
    
    def zmien1(self,nowa_cena):
        self.cena = nowa_cena

    def inf1(self):
        print(self.cena)

class Dzialo():
    def __init__(self,kaliber) -> None:
        self.kaliber = kaliber
    
    def zmien2(self, nowy_kaliber):
        self.kaliber = nowy_kaliber

    def inf2(self):
        print(self.kaliber)

class Silnik:
    def __init__(self,moc) -> None:
        self.moc = moc
    
    def zmien3(self,nowy_silnik):
        self.nowy_silnik = nowy_silnik

    def inf3(self):
        print(self.silnik)

class Zawieszenie:
    def __init__(self,wysokość_zawieszenia) -> None:
        self.wysokość_zawieszenia = wysokość_zawieszenia
    
    def zmien3(self, nowe_zawieszenie):
        self.nowe_zawieszene = nowe_zawieszenie

    def inf3(self):
        print(self.zawieszenie)

class Wieza:
    def __init__(self,prędkość_obrotu) -> None:
        self.prędkość_obrotu = predkość_obrotu
    
    def zmien3(self,nowa_predkość):
        self.nowa_predkość = nowa_predkość

    def inf3(self):
        print(self.wieza)

class Pancerz:
    def __init__(self,grubość) -> None:
        self.grubość = grubość
    
    def zmien3(self,nowa_grubość):
        self.nowa_grubość = nowa_grubość

    def inf3(self):
        print(self.wieza)


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

x.inf()
x.zmien()
x.inf()


