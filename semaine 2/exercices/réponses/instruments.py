class Instrument:
    def __init__(self, nom: str, famille: str, prix: float):
        self._nom = nom
        self._famille = famille
        self._prix = prix

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def get_famille(self):
        return self._famille

    def set_famille(self, famille):
        self._famille = famille

    def get_prix(self):
        return self._prix

    def set_prix(self, prix):
        self._prix = prix


class Guitare(Instrument):
    def __init__(self, nom: str, famille: str, prix: float, cordes: int):
        super().__init__(nom, famille, prix)
        self._cordes = cordes

    def get_cordes(self):
        return self._cordes

    def set_cordes(self, cordes):
        self._cordes = cordes

    def afficher(self):
        print(self._nom + " " + self._famille + " " + str(self._prix) + "$ " + str(self._cordes) + " cordes")

    def jouer(self):
        print("La guitare " + self._nom + " est en train de jouer: zing! zing!")


class Clarinette(Instrument):
    def __init__(self, nom: str, famille: str, prix: float, anches: int):
        super().__init__(nom, famille, prix)
        self._anches = anches

    def get_anches(self):
        return self._anches

    def set_anches(self, anches):
        self._anches = anches

    def afficher(self):
        print(self._nom + " " + self._famille + " " + str(self._prix) + "$ " + str(self._anches) + " anches")

    def jouer(self):
        print("La clarinette " + self._nom + " est en train de jouer: tut! tut!")


class Orchestre:
    def __init__(self):
        self._instruments = []

    def ajouter_instrument(self, instrument):
        self._instruments.append(instrument)

    def afficher(self):
        print("\nLes instruments de l'orchestre sont:")
        for instrument in self._instruments:
            instrument.afficher()

    def jouer(self):
        print("\nL'orchestre est en train de jouer:")
        for instrument in self._instruments:
            instrument.jouer()



guitare_electrique = Guitare("Fender", "cordes", 500, 6)
clarinette = Clarinette("Yamaha", "vent", 300, 1)
guitare_douze_cordes = Guitare("Gibson", "cordes", 700, 12)

orchestre = Orchestre()
orchestre.ajouter_instrument(guitare_electrique)
orchestre.ajouter_instrument(clarinette)
orchestre.ajouter_instrument(guitare_douze_cordes)

orchestre.afficher()
orchestre.jouer()