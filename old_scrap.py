from bs4 import BeautifulSoup          # For processing HTML
import requests
import random
from pprint import pprint
import json


# Fonctionne uniquement pour la partie chargée de la page (manque le reste en scrollant)
# Solution de faire une requete POST pour charger la suite ?
# NE MARCHE PAS
def scrap():
    url = 'https://www.youtube.com/c/JOYCA-JORDAN/videos'

    # Bypass le cookie Consent de Youtube
    page = requests.get(url, cookies={'CONSENT': 'YES+1'})

    # Autre solution
    # page = requests.get(url, cookies={'CONSENT': 'PENDING+999'})
    # page = requests.get(url,cookies={'CONSENT': 'YES+cb.20210328-17-p0.en-GB+FX+{}'.format(random.randint(100, 999))})

    # Recupération du dictionnaire données dans le script spécifique
    soup = BeautifulSoup(page.content, 'html.parser')
    res = soup.find_all('script')
    res = str(res[34])

    # On passe la string en JSON (dictionnaire)
    dictString = res.split('var ytInitialData =')
    dictString = dictString[1][:-10]
    dataJson = json.loads(dictString)

    # On isole la section de contenu qui nous interresse
    dataJson = dataJson['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']
    dataJson = \
    dataJson['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer'][
        'items']

    # Récupération des titres
    titles = []
    for video in dataJson:
        if 'gridVideoRenderer' in video:
            titles.append(video['gridVideoRenderer']['title']['runs'][0]['text'])
    pprint(titles)

if __name__ == '__main__':
    scrap()
