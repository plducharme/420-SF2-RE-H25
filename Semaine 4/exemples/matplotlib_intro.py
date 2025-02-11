import matplotlib.pyplot as plt
import numpy as np


# Créer un graphique à partir de données
# Les données sont des listes de valeurs
valeurs_x = [1, 2, 3, 4, 5]
valeurs_y = [1, 4, 9, 16, 25]
plt.plot(valeurs_x, valeurs_y)
plt.show()

# On peut passer des paramètres pour personnaliser le graphique
# marker : forme des points
# color : couleur de la ligne
# linestyle : style de la ligne
plt.plot(valeurs_x, valeurs_y, marker="o", color="red", linestyle="--")
plt.show()

# On peut aussi utiliser la notation MATLAB pour personnaliser le graphique
plt.plot(valeurs_x, valeurs_y, "yo-")
plt.show()

# On peut "plotter" plusieurs courbes sur le même graphique
valeurs_y = np.arange(1, 10)
valeurs_y_carre = valeurs_y ** 2
valeurs_y_x3 = valeurs_y * 3
plt.plot(valeurs_y, valeurs_y, "r--", valeurs_y, valeurs_y_carre, "bs", valeurs_y, valeurs_y_x3, "g^")
plt.show()

# On peut ajouter des labels aux axes, une légende et un titre
plt.plot(valeurs_y, valeurs_y, "r--", valeurs_y, valeurs_y_carre, "bs", valeurs_y, valeurs_y_x3, "g^")
plt.legend(["y = x", "y = x^2", "y = 3x"])
plt.title("Courbes de fonctions")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# Voir: https://matplotlib.org/stable/tutorials/pyplot.html


