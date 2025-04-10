# Écriture dans un fichier
with open('text.txt', mode='w', encoding='UTF8') as fichier_txt:
    fichier_txt.write('Si les cochons avaient des ailes, ça ferait de beaux serins.\n')
    # Affiche la classe implémentant le writer
    print(type(fichier_txt))
    # Écrire un caractère à partir de son code utf-8
    fichier_txt.write('\u274C\n')



