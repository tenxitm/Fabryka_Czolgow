
class Magazyn:
    def __init__(self, _cena) -> None:
        self.magazyn = []
        self.na_sprzedarz = []
        self.cena = _cena

    def doaj_czolg_do_magazynu(self, czolg):
        self.magazyn.append(czolg)
    
    
    def dodaj_czolg_na_sprzedarz(self, czolg):
        self.magazyn.append(czolg)
    
    def usun_czolg_z_magazynu(self, czolg):
        self.magazyn.remove(czolg)
    
    def usun_czolg_sprzedarz(self, czolg):
        self.magazyn.remove(czolg)

    def przenies_czolg_z_magazynu_na_sprzedarz(self, czolg):
        self.magazyn.remove(czolg)
        self.na_sprzedarz.append(czolg)

    def zmien_cene(self, nowa_cena):
        self.cena = nowa_cena
.
