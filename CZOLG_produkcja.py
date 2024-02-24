class Czolg:
  def __init__(self,dzialo,silnik)
    self.dzialo = dzialo
    self.silnik = silnik

class elementy_czolgu:
  def __init__(self,nazwa,numer_seryjny,cena):
    self.nazwa=nazwa
    self.numer_seryjny=numer_seryjny
    self.cena=cena

class Dzialo(elementy_czolgu):
    def __init__(self,nazwa,numer_seryjny,cena,kaliber):
        super().__init__(nazwa,numer_seryjny,cena)
        self.kaliber=kaliber

    def edytuj_kaliber(self,nowy_kaliber):
        self.klaiber=nowy_kaliber

class Silnik(elementy_czolgu):
    def __init___(self,nazwa,numer_seryjny,cena,moc):
        super().__init__(nazwa,numer_seryjny,cena)
        self.moc=moc

    def edytuj_moc(self,nowa_moc):
        self.moc=nowa_moc
#na razie wystarczy
#===========================================================

