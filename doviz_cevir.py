#TCMB Sitesinden efektif dolar satış fiyatını çekelim

from bs4 import *

import requests

sayfa=requests.get("https://www.turkiye.gov.tr/doviz-kurlari")
print(sayfa.text)

soup=BeautifulSoup(sayfa.text, "html.parser")

efektif_dolar_satis=soup.find('td',text='1 ABD DOLARI')\
    .find_next_sibling('td').\
    find_next_sibling('td').\
    find_next_sibling('td').\
    find_next_sibling('td').text

print("Dolar Satış",efektif_dolar_satis)