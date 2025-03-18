import math

import matplotlib.pyplot as plt


def poly(valeur):
    return math.factorial(valeur)


nombre = []
valeur = []
for i in range(1, 150):
    nombre.append(i)
    valeur.append(poly(i))

plt.plot(nombre, valeur)
plt.xlabel('valeur de n')
plt.ylabel('valeur du résultat de la fonction')
plt.ylim((0, 100))
plt.show()