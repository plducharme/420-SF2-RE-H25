class Personnage:

    def __init__(self):
        print("Personnage créé")


# Comme on défini un constructeur, le constructeur de la classe parent n'est pas appelé automatiquement,
# il faut le faire explicitement
class Corsaire(Personnage):

    def __init__(self):
        super().__init__()
        print("Corsaire créé")


# Comme on ne définit pas de constructeur, le constructeur par défaut est appelé. Celui-ci appelle le constructeur de
# la classe parent, qui lui aussi appelle le constructeur de sa classe parent, etc.
class Albator(Corsaire):

    pass


albator = Albator()

