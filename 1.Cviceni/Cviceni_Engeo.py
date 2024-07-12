"""
list = ["Frantisek", "Bruno", "Anna", "Jakub", "Klara", "Anezka", "Anezka", "Anezka"]
posledni_index = len(list)-1
print(list[posledni_index])

print("Na indexu 2 je:", list[2])
print("Na indexu 7 je:", list[7])
print("V intervalu od 2 do 5 je:", list[2:6])
print("Každý třetí člen je :", list[::3])
"""
"""
#palindrom
zadana_slova = ["jaro", "jej", "kolo", "aha"]
slovo = zadana_slova[1]
palindrom = slovo[::-1]

if slovo == palindrom:
    print("slovo", slovo, "je palindrom")
else:
    print("slovo", slovo, " neni palindrom")
"""

"""
zamestnanci = ["Frantisek", "Anna", "Jakub", "Klara"]
print("Zamestnanci na zacatku:", zamestnanci)

zamestnanci_a = zamestnanci.copy()
zamestnanci_a.append("Bruno")
zamestnanci_a.append("Anezka")
print("Nova jmena pridana:", zamestnanci_a)

zamestnanci_b = zamestnanci_a.copy()
zamestnanci_b.insert(1, "Bruno")
print("Nova jmena vlozena:", zamestnanci_b)
"""

"""
vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')

cislo_dne = 3

if cislo_dne in vstupni_cisla:
    print("Správná vstupní hodnota!")
    den_tydne = tyden[cislo_dne - 1]
    if den_tydne[0] == vstupni_pismena[cislo_dne-1]:
        print("Správné písmeno")
    else:
        print("Špatné písmeno")
else:
    print("Špatná vstupní hodnota!")    
"""
"""
kandidati = ["Bruno", "Anežka"]
zamestnanci = ['František', 'Bruno', 'Anna', 'Jakub', 'Klára']

bez_bruna = kandidati.copy()
bez_bruna.remove("Bruno")
print("Bruno odstraněn:", bez_bruna)

opakovani_kandidati = 3*bez_bruna
print("Opakování kandidáti:", opakovani_kandidati)

spojeni_zamestnanci = zamestnanci + opakovani_kandidati
print("Spojení zaměstnanci:", spojeni_zamestnanci)
"""
"""
#BMI Karkulacka
vyska = 2
vaha = 80
jmeno = 'Martin'

bmi = vaha / vyska ** 2
if bmi > 40:
    kategorie = 'těžká obezita'
elif bmi > 30:
    kategorie = 'obezita'
elif bmi > 25:
    kategorie = 'mírná nadváha'
elif bmi > 18.5:
    kategorie = 'zdravá váha'
else:
    kategorie = 'podvýživa'

print(jmeno, "tvé BMI je", bmi, ", což spadá do kategorie", kategorie, ".")
"""

"""
zadana_slova = ["Matous", "Martin", "ahoj","er", "es", "i", "a"]
slovo = zadana_slova[1]
delka_slova = len(slovo)

if delka_slova >= 4:
    print(slovo, "počet znaků:", delka_slova)
elif delka_slova > 3 and delka_slova < 1:
    print(slovo, "počet znaků: 2")
elif delka_slova == 1:
    print(slovo, "počet znaků:1")
"""
"""
#Sety 
cisla_1 = (1, 1, 2, 3, 4)
cisla_2 = (5, 6, 7, 7, 8)
cisla_1 = set(cisla_1)
cisla_2 = set(cisla_2)
sjednocene_hodnoty = cisla_1.union(cisla_2)
print("Sjednocené hodnoty ze zadání:", sjednocene_hodnoty)
"""
"""
cisla_1 = {1, 2, 3, 4}
cisla_2 = {3, 4, 5, 6}
rozdil_cisel = cisla_1.difference(cisla_2)
print("Rozdílné hodnoty prvního setu oproti druhému:", rozdil_cisel)
"""

"""
##Dictionary
user_1 = {}
user_email = {"email":"marek.parek@gamil.com"}
user_1['name'] = "Marek"
user_1['surname'] = "Parek"
user_1.update(user_email)
print("User#01",user_1)
"""
"""
employees = {
    'employee01': {
        'name': 'Marek',
        'surname': 'Parek',
        'email': 'marek.parek@gmail.com'
    },
    'employee02': {
        'name': 'Matous',
        'surname': 'Svatous',
        'email': 'matous.svatous@gmail.com'
    },
    'employee03': {
        'name': 'anna',
        'surname': 'rana',
        'email': 'anna.rana@gmail.com'
    }
}

print("Všechny klíče:", employees.keys())
print("Všechny hodnoty:", employees.values())
print("Všechny údaje k poslednímu zaměstnanci:",employees['employee03'].items())
"""
"""
#Pridani dict to dict pomoci klice
id123 = {'jmeno': 'Thomas', 'vek': 45, 'zeme': 'Czechia', 'mesto': 'Brno'}
id124 = {'jmeno': 'Daniel', 'vek': 34, 'zeme': 'Czechia', 'mesto': 'Prague'}
id125 = {'jmeno': 'Eva', 'vek': 43, 'zeme': 'Czechia', 'mesto': 'Olomouc'}

databaze = {'id123': {},'id124': {},'id125': {}}
databaze['id123'] = id123
databaze['id124'] = id124
databaze['id125'] = id125
print(databaze)
"""
"""
jmeno = 'Marek'
heslo = '1234'
uzivatel = {'Marek': '1234'}

if uzivatel.get(jmeno) == heslo:
    print("Ahoj",jmeno, "vítej v aplikaci! Pokračuj...")
else:
    print("Uživatelské jméno nebo heslo nejsou v pořádku!")
"""

"""
sequence = [1, 21, 5, 3, 5, 8, 321, 1, 2, 2, 32, 6, 9, 1, 4, 6, 3, 1, 2]
counts = {}

for i in sequence:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] = counts[i] + 1

sorted_counts = dict(sorted(counts.items()))

for key in sorted_counts:
    print("key:", key, "value:", counts[key])
"""

"""
vysledek = []
zadana_cisla = "1,2,3,4,5"
cisla = zadana_cisla.split(",")

for i in cisla:
    ocisene_cislo = int(i.strip())
    vysledek.append(ocisene_cislo)

print("List:", vysledek)
"""
"""
veta = "Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu"
samohlasky = "aeiouáéíóú"
souhlasky = "bcčdďfghjklmnňprřsštťvzžcdž"
vysledek = {"souhlasky":0, "samohlasky":0}

for i in veta:
    if i.lower() in samohlasky:
        vysledek["samohlasky"] = vysledek["samohlasky"] + 1
    elif i.lower() in souhlasky:
        vysledek["souhlasky"] = vysledek["souhlasky"] + 1
    else:
        continue

print("Pocet souhlasek:", vysledek["souhlasky"], "| Pocet samohlasek", vysledek["samohlasky"])
"""      
"""
cisla = [1, 2, 3, 4, 5, 6, 7, 8]
suda = 0 
licha = 0

for i in cisla: 
    if i % 2 == 0:
        suda += i 
    else:
        licha += i 

vysledek = abs(suda - licha)
print("Rozdil je :", vysledek)
"""
"""
for i in range(1,101):
    if (i % 5 == 0) and (i % 3 == 0): 
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
"""
"""
vysledek = list()
start = 3
stop = 9
delitel = 3

if isinstance(start,int) and isinstance(stop,int) and isinstance(delitel,int):
    for i in range(start,stop+1):
        if i % delitel == 0:
            vysledek.append(i)
        else:
            continue
    print("#Start:",start,", Stop:", stop,", Delitel:", delitel)
    print("Zadany rozsah: <",start,stop,">")
    print("Cisla delitelna", delitel,":", vysledek)
else:
    print("#Start:",start,", Stop:", stop,", Delitel:", delitel)
    print("Zadane vstupy musi byt cisla")
"""
"""
jmena = [
 'Michal', 'Pepa', 'Honza',
 'Pavel', 'Lukas', 'Matej',
 'Iva', 'Klara', 'Jana',
 'Honza', 'Vasek','Milan',
 'Michal'
]

kopie_jmen = jmena.copy()
jmena = list(enumerate(jmena))

# Iterace k získání indexů v listu "jmena"
for i in range(len(kopie_jmen)):
    # Iterace k získání indexu, který je o 1 vyšší než aktuální hodnota i
    for j in range(i + 1, len(kopie_jmen)):
        # Pokud je hodnota na indexu i větší než hodnota na indexu j aktualizuj
        # ..pořadí hodnot v listu za pomocí indexů
        if kopie_jmen[i] > kopie_jmen[j]:
            kopie_jmen[i], kopie_jmen[j] = kopie_jmen[j], kopie_jmen[i]
# Vypiš výsledek
print(kopie_jmen)
"""
"""
velikost = 10
symboly = ['#',' ']
sachovnice = []
# Iteruj přes řádky šachovnice a vytvoř proměnnou "rada"
for radek in range(velikost):
    rada = []
    # Iteruj přes jednotlivé buňky v každém řádku
    for bunka in range(velikost):
        # Vytvoř index, který vybere jednu z hodnot v proměnné "symboly"
        index = (radek + bunka) % len(symboly)
        rada.append(symboly[index])
    # Přidej hotové buňky do proměnné "sachovnice"
    sachovnice.append(''.join(rada))
# Vypiš výslednou šachovnici
print('\n'.join(sachovnice))
"""

"""
seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]
delky_slov = {}

for i in seznam_slov:
    delky_slov.update({i:len(i)})

print(delky_slov)
"""

"""
slova = []
while len(slova) < 3:
    slovo = input("ZADEJ SLOVO ZE ČTYŘ:")
    if slovo in slova:
        print("Slovo", slovo,"uz je ulozene")
    elif len(slovo) != 4:
        print("Slovo není dlouhé čtyři znaky")
    else:
        slova.append(slovo)
else:
    print("Už mám uložené tři slova")    
"""
"""
ovoce = ["jablko", "banan", "citron", "pomeranc"]
print("Dostupne ovoce", ", ".join(ovoce))

while True: 
    vyber = input("VYBER Z DOSTUPNÉHO OVOCE:") 
    if vyber in ovoce: 
        nabidka = 0
        print("Bezva, toto ovoce je v nabídce.")
        break 
    else:
        print("Ovoce není v nabídce.")
"""            
"""
while True:
    operation = input("Vyber operator (+ , - ): ")
    operators = ["+","-"]
    
    if operation in operators:
        number_1 = int(input("Zadej první číslo:"))
        number_2 = int(input("Zadej druhe číslo:"))

        if operation == '+':
            print(f'{number_1} + {number_2} = {number_1 + number_2}')
        else:
            print(f'{number_1} - {number_2} = {number_1 - number_2}')
        
        again = input('Chcete provést další operaci?(a pro ano, jakákoliv jiná klávesa pro ne): ')
        if again == "a":
            continue
        else:
            print("ukoncuji")
            break
    else:
        print("Nezadali jste platný operátor, zkuste to znovu")
"""
