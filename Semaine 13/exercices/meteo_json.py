import requests
import json


class MeteoApi:

    @staticmethod
    def prevision_meteo(latitude=45.617481, longitude=-72.975096):
        # Fait un appel à l'API Open Meteo pour obtenir les prévisions météo sur un serveur distant
        reponse = requests.get(f"https://api.open-meteo.com/v1/gem?latitude={latitude}&longitude={longitude}"
                               f"&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset&timezone=America%2FNew_York")
        json_recu = reponse.json()
        print("json reçu:\n" + str(json_recu))
        return json_recu


meteo = MeteoApi.prevision_meteo()

