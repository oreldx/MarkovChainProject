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
    # titles = soup.find('a', class_='yt-simple-endpoint style-scope ytd-grid-video-renderer')

