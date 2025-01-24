# https://www.geeksforgeeks.org/personal-voice-assistant-in-python/
import os

import speech_recognition as sr
from googletrans import Translator
import playsound3  # to play saved mp3 file
from gtts import gTTS  # google text to speech


class Amanda:

    def __init__(self):
        self.numero_fichier = 0

    def amanda_dit(self, texte: str):
        self.numero_fichier += 1
        tts = gTTS(text=texte, lang='fr')
        fichier = f"audio{self.numero_fichier}.mp3"
        tts.save(fichier)
        playsound3.playsound(fichier)
        os.remove(fichier)

    def enregister_usager(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Ecoute...")
            audio = r.listen(source, timeout=5)
            try:
                texte = r.recognize_google(audio, language='ca-FR')
            except:
                self.amanda_dit("Je n'ai pas compris ce que vous avez dit")
                return None
            return texte

    def executer_commande(self, texte: str):
        texte = texte.lower()
        print(texte)
        if "au revoir" in texte:
            self.amanda_dit("Au revoir")
            exit()
        elif "comment vas-tu" in texte:
            self.amanda_dit("Je vais bien, merci!")
        elif "qui es-tu" in texte:
            self.amanda_dit("Je suis Amanda, la meilleure assistante personnelle")
        elif "traduire" in texte:
            texte_a_traduire = texte.split("traduire")[1]
            traducteur = Translator()
            traduction = traducteur.translate(texte_a_traduire, src='fr', dest='ar')
            self.amanda_dit(traduction.text)
        else:
            self.amanda_dit("Je n'ai pas compris ce que vous voulez dire")

    def boucle(self):
        while True:
            amanda.amanda_dit("Je suis Amanda, votre assistante personnelle. Comment puis-je vous aider?")
            texte = self.enregister_usager()
            if texte is not None:
                self.executer_commande(texte)


amanda = Amanda()
amanda.boucle()
