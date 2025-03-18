import matplotlib.pyplot as plt

def constante(valeur):
    return 1


nombre = []
valeur = []
for i in range(0, 11):
    nombre.append(i)
    valeur.append(constante(i))

plt.plot(nombre, valeur)
plt.show()
