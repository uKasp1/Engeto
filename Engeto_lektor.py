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
