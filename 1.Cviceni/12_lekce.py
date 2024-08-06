"""
import matplotlib.pyplot as plt

x = [45, 56, 78]
y = [23, 45, 65]

plt.plot(x, y)
plt.show()

print('Jak se vám zatím líbí poslední lekce?') 
"""

## Webscraping 

import requests
from bs4 import BeautifulSoup
from pprint import pprint

url_1 = "https://heroes3.cz/hraci/index.php?page=1&order=&razeni=DESC"
url_2 = "https://heroes3.cz/hraci/index.php?page=2&order=&razeni=DESC"

odp_serveru = requests.get(url_1)
#print(odp_serveru)
type(odp_serveru.text)
#print(odp_serveru.text)
#print(odp_serveru.text[:16])

soup = BeautifulSoup(odp_serveru.text, 'html.parser')   # promenna + typ parseru
#print(soup)
#print(type(soup))
#dir(soup)
isinstance(soup, BeautifulSoup)
#print(soup.prettify())

table_tag_top = soup.find("table", {"class": "tab_top"})
#print(table_tag_top.prettify())

vsechny_tr = table_tag_top.find_all("tr")
#print(vsechny_tr)
#print(vsechny_tr[1])

for tr in vsechny_tr[1:]:             # vynechame zahlavi, budeme mit vlastni
    td_na_radku = tr.find_all("td")
    print(td_na_radku[1].get_text())  # Pozor, seznam bunek
    break                           # po prvnim cyklu ukoncime


pprint(td_na_radku)
print(td_na_radku[0].get_text())
print(td_na_radku[2].text)
print(td_na_radku[2].string)
print(td_na_radku[2].getText())

def vyber_atributy_z_radku(tr_tag: "bs4.element.ResultSet"):
    
    #Z kazdeho radku (tr) vyber urcite bunky (td)[index])
    #   a zabal je do slovniku
    
    return {
        "poradi": tr_tag[0].getText(),
        "jmeno": tr_tag[2].getText(),
        "vitezstvi": tr_tag[5].getText(),
        "celkem_her": tr_tag[6].getText()
    }
vysledky = []

# 1. zapis 
for tr in vsechny_tr[1:]:
    td_na_radku = tr.find_all("td")
    data = vyber_atributy_z_radku(td_na_radku)
    vysledky.append(data)

pprint(vysledky)
pprint("="*150)

data_o_hracich: list = list()

# kratsi zapis 
for tr in vsechny_tr[1:]:
    data_o_hracich.append(vyber_atributy_z_radku(tr.find_all("td")))
pprint(data_o_hracich)
pprint("="*150)

# list comprehation 
data_o_hracich1 = [
    vyber_atributy_z_radku(tr.find_all("td"))
    for tr in vsechny_tr[1:]
]

pprint(data_o_hracich1)


# API 
"""
import requests
from pprint import pprint

url = 'https://aoe2.net/api/leaderboard'
params = {
    'game': 'aoe2de', 
    'leaderboard_id': '3', 
    'start':'1',
    'count':'100'
    }
    
response = requests.get(
    url, 
    params=params, 
    )

if response.status_code == 200:
    data = response.json()
    pprint(data)
else:
    print('Chyba při získávání dat')
"""




