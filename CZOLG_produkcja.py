
class Dzialo:
    def __init__(self,kaliber) -> None:
        self.kaliber = kaliber
    
    def zmien(self, nowy_kaliber):
        self.kaliber = nowy_kaliber

    def inf(self):
        print(self.kaliber)

class Silnik:
    def __init__(self,moc) -> None:
        self.moc = moc
    
    def zmien(self,nowy_silnik):
        self.moc = nowy_silnik

    def inf(self):
        print(self.moc)

class Zawieszenie:
    def __init__(self,wysokość_zawieszenia) -> None:
        self.wysokość_zawieszenia = wysokość_zawieszenia
    
    def zmien(self, nowe_zawieszenie):
        self.wysokość_zawieszenia = nowe_zawieszenie

    def inf(self):
        print(self.wysokość_zawieszenia)

class Wieza:
    def __init__(self,predkość_obrotu) -> None:
        self.prędkość_obrotu = predkość_obrotu
    
    def zmien(self,nowa_predkość):
        self.nowa_predkość = nowa_predkość

    def inf(self):
        print(self.wieza)

class Pancerz:
    def __init__(self,grubość) -> None:
        self.grubość = grubość
    
    def zmien(self,nowa_grubość):
        self.nowa_grubość = nowa_grubość

    def inf(self):
        print(self.pancerz)

class Czolg():
    ilosc = 0
    def __init__(self,cena):
        self.dzialo = Dzialo(1)
        self.silnik = Silnik(1)
        self.zawieszenie = Zawieszenie(1)
        self.wieza = Wieza(1)
        self.pancerz = Pancerz(1)
        self.cena = cena
        Czolg.ilosc += 1
        self.numer_seryjny = Czolg.ilosc

    # def inf(self):
    #     self.elm1.inf1()
    #     self.elm2.inf2()
    #     self.elm3.inf3()
    
    # def zmien(self):
    #     self.elm1.zmien1()
    #     self.elm2.zmien2()
    #     self.elm3.zmien3()


