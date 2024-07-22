"""
animals = ["cat", "dog", "rabbit"]
 
for index, animal in enumerate(animals):
    print(index, animal)

A = [[1,2,3], [4,5], [6,7,8,9]]
B = []

for x in A:
    for y in x:
        B.append(y)
print(B)
"""

"""
a = 0 
print("Do you want to continue")
for i in range(3):
    x = input()
    if  x == "y":
        print("--> Continue")
        break
    else:
        if i == 2:
        else:
            continue
"""
"""
# fibonacciho posloupnost 
i = 0 
f = [0,1]

while i < 16:
    f.append(f[i]+f[i+1])
    print(f[i], f[i+1])
    print(i)
    print(f)
    print("_______________")
    i +=1
print(f)
"""
"""
letters = ["a","a","b","c","d","a","e","g","m"]

while len(letters):
    delete = input("ktere pismeno chces odstranit? ")
    if delete in letters:
        letters.remove(delete)
        print(letters)
    else:
        print("Pismeno neni v seznamu")
print("seznam je prazdny")
"""
#Lekce 9
"""
muj_string = "Prave probiha lekce 9"
muj_soubor = open("lekce_9.txt", mode="w") #mode writer 
muj_soubor.write(muj_string) 
muj_soubor.close()     

muj_string2 = "\nPrave pokracuje lekce 9"
muj_soubor = open("lekce_9.txt", mode="a") #mode append  
muj_soubor.write(muj_string2) 
muj_soubor.close()  

muj_string3 = "\nPrave pokracuje lekce 9" #pomoci \n zapiseme text na novy radek tak at se mi to 
muj_string4 = "\nPrave pokracuje lekce 9" #v modu write nep5episuje 
muj_string5 = "\nPrave pokracuje lekce 9"
muj_soubor = open("lekce_9_1.txt", mode="w")   
muj_soubor.write(muj_string3)
muj_soubor.write(muj_string4) 
muj_soubor.write(muj_string5)  
muj_soubor.close()  
"""
"""
muj_existujici_soubor = open("lekce_9.txt")
print(muj_existujici_soubor)
print(muj_existujici_soubor.read())
obsah_txt = muj_existujici_soubor.read()
print(obsah_txt) #Pokud chci precist soubor podruhe nic neuvidim proto6e pomyslny kurzor je na konci 
#textu tudiz nic nevidi
# Pomoci metody seek lze tento kurzor presunout

muj_existujici_soubor.seek(0) #Presune kurzor na zacatek souboru
muj_existujici_soubor.seek(0,2) #Presune kurzor na konec souboru
muj_existujici_soubor.seek(0) 
print(muj_existujici_soubor.read())

# Metody 
# read = cely radek
# readline = pouze prvni radek jako string 
# readlines = precte cely soubor jako list (co radek to udaj)
muj_existujici_soubor.seek(0)
#Kazdy radek precte jeden radek 
print(muj_existujici_soubor.readline())
print(muj_existujici_soubor.readline())
print(muj_existujici_soubor.readline())
print(muj_existujici_soubor.readline())
print(muj_existujici_soubor.readline())

muj_existujici_soubor.seek(0)
#ulozi jako list
print(muj_existujici_soubor.readlines())
muj_existujici_soubor.close()


muj_soubor1 = open("lekce_9_2.txt", mode="r+") #pro cteni a zapis
print(muj_soubor1.read())
muj_soubor1.write("\njeste jeden radek")
print(muj_soubor1.tell())

with open("lekce_9_2.txt", mode="a") as muj_soubor1:
    muj_soubor1.write("\n A jeste jeden radek s textoveho manazera")
"""
"""
import os 
from pprint import pprint
#Cvicei lekce 9
def start_prevod(absolutni_cesta, vzor):
    #print(absolutni_cesta) #vzcteni cesty k souboru
    #pprint(nacteni_souboru(absolutni_cesta)) #nacteni dat ze souboru
    byty = nacteni_souboru(absolutni_cesta, vzor)
    iteruj_data(byty, vzor)

def nacteni_souboru(soubor):
    with open(soubor, mode="r", encoding="UTF-8") as txt:
        return txt.readlines()              

def iteruj_data(data, vzor):
    for detail in data:
        print(prepis_byt(detail, vzor))

def prepis_byt(detail, vzor):
    dispozice, zbytek  = detail.split(",", maxsplit = 1)[0]
    novy_zapis = vzor.get(dispozice)
    print(novy_zapis)

def prevod_typu():
    absolutni_cesta = f"{os.getcwd()}{os.sep}vstupni_data.txt" #dostan absolutni cestu od souboru
    prevodni_vzor = {
        "byt0001": "1+1",
        "byt0002": "2+1",
        "byt0003": "2+kk",
        "byt0004": "3+1",
        "byt0005": "3+kk",
        "byt0006": "4+1",
        "byt0007": "4+kk",
        }
    
    start_prevod(absolutni_cesta, prevodni_vzor)

prevod_typu()
"""

# Lekce 10 
"""
vysledky = {
    "11.11.2010":135,
    "11.11.2015":130,
    "11.11.2020":133,
}

for i, data in enumerate(vysledky.items()):
    if i == 0:
        print(f"|{"Datum":^10}|{"Body":^5}|")
    print(f"|{data[0]:^10}|{data[1]:^5}|")

print(f"|{"Datum":^10}|{"Body":^5}|")
for i, data in vysledky.items():
    print(f"|{i:^10}|{data:^5}|")
"""
#Lekce 10. cviceni
"""
import os 
from pprint import pprint

# promene 
txt_soubor = "countries_and_cities.txt"

# nacti txt soubor 
def nacteni_txt(jmeno):
    try:
        with open(jmeno, mode="r", encoding="UTF-8") as txt:
            obsah = txt.readlines()

    except FileNotFoundError:
        print(f"Soubor {jmeno} nenalezen",
              f"Adresa: {os.getcwd()}",
              f"Obsah slozky: {os.listdir()}",
              sep="\n"
              )
    else:
        print(f"Soubor {txt_soubor} nacten")
        return obsah
    finally:
        print("Konec funkce")

# funkce zformatuje nazvy 

def zformatuj_nazvy():
    for udaj in nacteni_txt(txt_soubor):
        pprint(f"{udaj=}")


print(zformatuj_nazvy())
"""

# Lekce 11
"""
import csv 

hlavicka = ["jmeno", "prijmeni", "email","telefon"]
osoba_1 = ["Radim", "Jedlicka", "radim@gmail.com","987654321"]
osoba_2 = ["Jaroslav", "Tylich", "jarda@engeto.cz","321654987"]

csv_soubor = open(
    "engeto_lide_python.csv",
    mode="w",
    encoding="UTF-8",
    newline=""  # None
)
print(csv_soubor)
zapisovac = csv.writer(csv_soubor, delimiter=",")

#zapisovac.writerow(hlavicka)
#zapisovac.writerow(osoba_1)
#zapisovac.writerow(osoba_2)  # writerows(iterable)
zapisovac.writerows((hlavicka,osoba_1,osoba_2))
csv_soubor.close()


#dictWriter
osoba_3 = {"jmeno": "Matous", "prijmeni": "Pokoj", "vek": "28"}
osoba_4 = {"jmeno": "Petr", "prijmeni": "Svetr", "vek": "27"}

dalsi_csv = open(
    "engeto_lide_linux.csv",
    mode="w",
    encoding="utf-8",
    newline=""
)

zapisovac = csv.DictWriter(dalsi_csv, fieldnames=osoba_3.keys())
zapisovac.writeheader()
zapisovac.writerow(osoba_3)
zapisovac.writerow(osoba_4)
zapisovac.writerows((osoba_3, osoba_4))
dalsi_csv.close() 
"""
"""
# Precti csv soubor 
obsah_csv = open(
    "engeto_lide_linux.csv",
    encoding="utf-8",
    mode="r"  # Default
)

cteni = csv.reader(obsah_csv)
print(cteni)

for radek in cteni:
    print(radek)
obsah_csv.close()

# DictReader 
moje_csv = open(
    "engeto_lide_linux.csv",
    mode="r",
    encoding="utf-8"
)
obsah = csv.DictReader(moje_csv)
print(tuple(obsah))
moje_csv.close()

# Kontextovy manager 

jmeno_csv = "engeto_lide_linux.csv"
with open(jmeno_csv, encoding="utf-8", mode="r") as csv_soubor:
    cteni = csv.DictReader(csv_soubor)
    for zaznam in cteni:
        print(zaznam)
"""

# JSON files 
"""
import json

chuckuv_slovnik = {
    "jmeno": "Chuck Norris",
    "neuspech": None,
    "kliky": "vsechny",
    "konkurence": False,
    "doplneni": "Łukasz",
}

print(type(chuckuv_slovnik))

vypis_json = json.dumps(chuckuv_slovnik)  # výstup pouze jako str
print(vypis_json)
print(type(vypis_json))

json_soubor = open(
    "prvni_JSON.json",
    mode="w",
    encoding="UTF-8"
)

json.dump(chuckuv_slovnik, json_soubor)
json_soubor.close()

# Kontextovy manazer 
with open("prvni_JSON.json", mode="w", encoding="UTF-8") as json_soubor:
    json.dump(chuckuv_slovnik, json_soubor)  # CO, KAM

# Nacti existujici soubor 
existujici_json = open("prvni_JSON.json", mode="r", encoding="UTF-8")
print(existujici_json)
obsah_json = json.load(existujici_json)
print(obsah_json)
print(type(obsah_json))
existujici_json.close()

# Nacti pomoci kontext manazera 
with open("prvni_JSON.json", mode="r", encoding="UTF-8") as existujici_json:
    obsah_json = json.load(existujici_json)  # CO

print(obsah_json)
existujici_json.closed

json_str = json.dumps(
    chuckuv_slovnik,
    ensure_ascii=False,  # False zapíše původní znak, True zapíše reprezentaci znaku pomocí lomítek.
    indent=4, # odsadí zapsaný json o 4 mezery
    sort_keys=True #  seřadí klíče (True/False)
)

# Zapis s kontextovym manazeram 

with open("druhy_JSON.json", mode="w", encoding='UTF-8') as json_soubor:
    json.dump(
        chuckuv_slovnik,
        json_soubor,
        ensure_ascii=False,
        indent=4,
        sort_keys=True
    )

json_soubor.closed
"""
"""
# Systemovy argument SYS.ARGV

import sys 
# nefunguje 
print("Jméno spuštěného programu:", sys.argv[0])
if len(sys.argv) > 1:
    print("Byl předán argument:", sys.argv[1])
else:
    print("Nebyl předán žádný argument.")

# Načtení seznamu z nákupního listu
with open("shopping_list.txt", "r") as f:
    shopping_list = f.read().splitlines()

print("Původní nákupní seznam:")
print(shopping_list)

# Přidání nových položek na konec seznamu
if len(sys.argv) > 1:
    for item in sys.argv[1:]:
        shopping_list.append(item)

# Vypsání upraveného seznamu
print("Upravený nákupní seznam:")
print(shopping_list)

# Uložení seznamu zpět do souboru
with open("shopping_list.txt", "w") as f:
    for item in shopping_list:
        f.write(item + "\n")
"""

# Lekce 11. Cviceni 

import os 
import json
import csv
from pprint import pprint

# TODO: Relativni cesta souborem 
rel_cesta = "solution/"

# TODO Potrebne klice 
zadouci_klice = ["first_name", "last_name", "email"]

# TODO fce json_to_csv 
def json_to_csv():
    jsony = najdi_json(rel_cesta)

    obsah_json = []
    for soubor in jsony:
        for zaznam in precti_json(soubor):
            obsah_json.append(filtr_klicu(zadouci_klice, zaznam))

    zapis_csv("soubor1.csv", obsah_json)

# TODO funkce, ktera najde vsechny json soubory 
def najdi_json(adresar):
    list_souboru = []
    for jmeno in os.listdir(adresar):
        if os.path.splitext(jmeno)[1] == ".json" and "_" in jmeno:
            list_souboru.append(jmeno)
    return list_souboru

# TODO funkce, ktera nacte obsah souboru 
def precti_json(jmeno):
    try:
        soub_json = open(os.path.join("solution", jmeno), "r", encoding="UTF-8")
    except FileNotFoundError:
        print("File not found")
    else:
        lide_info = json.load(soub_json)
        soub_json.close()
        return lide_info

# TODO funkce, ktera upravi obsah souboru 
def filtr_klicu(zadouci:list, puvodni_zaznam:dict):
    vycistene_zaznam = {}

    for klic in puvodni_zaznam.keys():
        if klic not in zadouci:
            continue
        vycistene_zaznam[klic] = puvodni_zaznam[klic]
    return vycistene_zaznam

# TODO funkce, ktera ulozi soubory do csv na lokal
def zapis_csv(jmeno_souboru:str, zaznamy:list):

    with open(jmeno_souboru, encoding="utf-8", mode="w") as csv_vystup:
        try:
            sloupecky = zaznamy[0].keys()
        except IndexError:
            print("Problem s indexem")
        except FileExistsError:
            print("Nemuzu prepsat existujici soubor")
        else:
            zapis = csv.DictWriter(csv_vystup, fieldnames=sloupecky)
            zapis.writeheader()
            zapis.writerows(zaznamy)
            print("soubor zapsan")


test = json_to_csv()
pprint(test)


