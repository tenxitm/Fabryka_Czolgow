class Pracownik:
    def __init__(self, imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja
        self.ocena_pracy = ocena_pracy
        self.doswiadczenie = doswiadczenie
        self.podgrupa = podgrupa

    def zmien_pensje(self, nowa_pensja):
        self.pensja = nowa_pensja

    def zmien_ocene_pracy(self, nowa_ocena):
        self.ocena_pracy = nowa_ocena

    def zmien_doswiadczenie(self, nowe_doswiadczenie):
        self.doswiadczenie = nowe_doswiadczenie

    def opis(self):
        print(f"Imię: {self.imie}")
        print(f"Nazwisko: {self.nazwisko}")
        print(f"Pensja: {self.pensja}")
        print(f"Ocena pracy: {self.ocena_pracy}")
        print(f"Doświadczenie: {self.doswiadczenie}")
        print(f"Podgrupa: {self.podgrupa}")


class Pracownik_Montazu(Pracownik):
    def __init__(self, imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa):
        super().__init__(imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa)


class Pracownik_IT(Pracownik):
    def __init__(self, imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa):
        super().__init__(imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa)


class Pracownik_Organizacji_Pracy(Pracownik):
    def __init__(self, imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa):
        super().__init__(imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa)


# Przykładowe użycie:
pracownik1 = Pracownik_Montazu("Ben", "Smajher", 3500, 4, 3, "elektryk")
pracownik2 = Pracownik_IT("Jay", "Ram", 5000, 5, 5, "programista")
pracownik3 = Pracownik_Organizacji_Pracy("Maximov", "Vitalin", 4000, 3, 2, "mechanik")

pracownik1.zmien_pensje(4000)
pracownik1.opis()
#===============================================================================================
#===============================================================================================
