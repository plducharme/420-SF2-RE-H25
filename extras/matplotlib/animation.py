import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


# Données
# Générer des arrays 1D de grandeur 100
valeurs_x = np.random.rand(100)
valeurs_y = np.random.rand(100)


# Créer une nouvelle figure
fig = plt.figure()
# On ajoute un axe à la figure qui prend toute la place (le tuple donne la grandeur du rectangle de l'axe,
# par rapport à la figure)
ax = fig.add_axes((0, 0, 1, 1), frameon=False)
scatter = ax.scatter(valeurs_x, valeurs_y)


# fonction appelée à chaque frame de l'animation
def mise_a_jour_animation(frame):
    scatter.set_sizes([x * np.sin(frame) for x in valeurs_x])
    print("Frame: ", frame)


plt.title("Animation")
animation = FuncAnimation(fig, mise_a_jour_animation, interval=200, save_count=100)
plt.show()
