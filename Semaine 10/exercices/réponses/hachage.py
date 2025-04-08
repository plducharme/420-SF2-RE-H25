class MonObjet:
    def __init__(self, valeur):
        self.valeur = valeur


o1 = MonObjet(1)
o2 = MonObjet(2)
o3 = MonObjet(1)
print(f"Hachage d'un integer : {hash(10)}")
print(f"Hachage d'une chaîne : {hash("Super Duper")}")
print(f"Hachage de l'objet o1: {hash(o1)}")
print(f"Hachage de l'objet o2: {hash(o2)}")
print(f"Hachage de l'objet o3: {hash(o3)}")
print(f"Hachage d'un float : {hash(3.14)}")
