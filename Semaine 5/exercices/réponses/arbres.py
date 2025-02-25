mots = ["programmation", "code", "prorogation", "procrastination", "proclamation", "protection", "coder", "amas", "amasser"]


class Lettre:
    def __init__(self, lettre):
        self.lettre = lettre
        self.enfants = {}
        self.fin = False

    def __repr__(self):
        return f"Noeud({self.lettre}, {self.fin})"

    def insertion(self, lettre, derniere_lettre=False):
        if lettre not in self.enfants:
            self.enfants[lettre] = Lettre(lettre)
            if derniere_lettre:
                self.enfants[lettre].fin = True


    def insertion_mot(self, mot):
        if len(mot) == 1:
            self.insertion(mot[0], True)
        else:
            self.insertion(mot[0])
            self.enfants[mot[0]].insertion_mot(mot[1:])


class Arbre:
    def __init__(self):
        self.racine = Lettre("")

    def ajouter_mot(self, mot):
        self.racine.insertion_mot(mot)

    # On parcours l'arbre pour vérifier le mot
    def verifier_mot(self, mot, noeud_lettre=None):
        if noeud_lettre is None:
            noeud_lettre = self.racine

        lettre = mot[0]
        if lettre in noeud_lettre.enfants:
            if noeud_lettre.enfants[lettre].fin and len(mot) == 1:
                return True
            else:
                return self.verifier_mot(mot[1:], noeud_lettre.enfants[lettre])
        else:
            return False

    # On parcours l'arbre en profondeur pour afficher tous les mots
    def afficher_mots(self, mot="", noeud_lettre=None):
        if noeud_lettre is None:
            noeud_lettre = self.racine
        for lettre, enfant in noeud_lettre.enfants.items():
            if enfant.fin:
                print(mot + lettre)
            self.afficher_mots(mot + lettre, enfant)


arbre = Arbre()
# Construction de l'arbre
for mot in mots:
    arbre.ajouter_mot(mot)


arbre.afficher_mots()

print(arbre.verifier_mot("procrastination"))
print(arbre.verifier_mot("procrastinatations"))


