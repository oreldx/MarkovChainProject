from bs4 import BeautifulSoup          # For processing HTML
import requests
import random

if __name__ == '__main__':

    url = 'https://www.youtube.com/c/BestOfTwitchFR1/videos'

    # Bypass Cookies Consent Youtube - Other solution
    # page = requests.get(url, cookies={'CONSENT': 'PENDING+999'})
    # page = requests.get(url,cookies={'CONSENT': 'YES+cb.20210328-17-p0.en-GB+FX+{}'.format(random.randint(100, 999))})

    page = requests.get(url, cookies={'CONSENT': 'YES+1'})

    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)
    res = soup.find_all('script')
    res = str(res[34])

    dictString = res.split('var ytInitialData =')
    dictString = dictString[1][:-10]
    # print(dictString)
    cursor = dictString.find('Vidéos')
    cursor += 34
    # JsonText = J3[0].decode('utf-8')
    #
    # s = json.loads(JsonText)
