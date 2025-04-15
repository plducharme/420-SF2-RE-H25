# Tests unitaires
- Créer un fichier contenant les tests unitaires pour la classe Bibliotheque du fichier bibliotheque.py
  - Assurez-vous de tester toutes les méthodes de la classe
  - Assurrez-vous de tester les cas limites

# Sérialisation et désérialisation
- Créer un fichier serialisation.py qui contient les fonctions de sérialisation et désérialisation pour la classe Bibliotheque
  - importer le module bibliotheque et la classe Bibliotheque
  - créer un objet Bibliotheque et effectuer des opérations sur celui-ci (ajouter, emprunter, ajouter, enlever)
  - Utiliser le module pickle pour sérialiser et désérialiser la classe
    - Créer le fichier bibliotheque.pkl contenant la classe Bibliotheque sérialisée
    - lire ce fichier pour désérialiser la classe
  - Vérifier que les données sont identiques entre le fichier original et le fichier désérialisé
    - Créer un fichier contenant les tests unitaires relatifs à serialisation.py

# Notes sur l'utilisation de modèles d'intelligence artificielle
- Pour entrainer un modèle d'intelligence artificielle, il faut beaucoup de données et de puissance de calcul.
- Une fois entrainé, le modèle peut être utilisé pour faire des prédictions sur de nouvelles données.
- Les modèles d'intelligence artificielle peuvent être utilisés pour résoudre des problèmes complexes dans divers domaines tels que la vision par ordinateur,
le traitement du langage naturel, la reconnaissance vocale, classification, etc.

# Utilisation de modèle d'intelligence artificielle sur un serveur distant
- Créer un compte gratuit sur [huggingface.co](https://huggingface.co/)
- Créer un token d'accès dans votre compte
  - cocher les cases "read" sous "Repositories"
  - cocher la case "Make calls to Inference Providers"
- Installer le module huggingface_hub 
  - pip install huggingface_hub (ou via PyCharm)
- Suivre les instructions:
  - https://huggingface.co/docs/inference-providers/index sous la section Python (deuxième partie de la section)
  - Faire un appel pour un modèle de complétion de conversation (chat)
  - Une fois que cela fonctionne, essayer avec un modèle de génération d'images
    
NB: Le compte gratuit vous donne un crédit de 10 cents par mois pour les appels d'Inférence (rouler un modèle sur un serveur distant via un fournisseur).
Ce n'est pas beaucoup, mais cela vous permet de tester le service. La génération d'images coûte plus cher que la génération de texte.

# Utilisation de modèle d'intelligence artificielle en local
Des exemples d'utilisation d'un modèle en local seront fournis dans la section "extras" cette semaine. Lorsque roulé
en local, le modèle n'est pas limité par le crédit de 10 cents par mois. Cependant, le temps de réponse dépend fortement de la puissance de votre machine.

# Reconnaisance faciale
- Analyser le code sous "extras/opencv" pour comprendre comment il fonctionne
- Amusez-vous à modifier le code pour faire des choses différentes

# Reconnaissance vocale
- Analyser le code sous "extras/reconnaissance_vocale" pour comprendre comment il fonctionne
- Amusez-vous à modifier le code pour permettre de répondre à des questions