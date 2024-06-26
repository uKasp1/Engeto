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

letters = ["a","a","b","c","d","a","e","g","m"]

while len(letters):
    delete = input("ktere pismeno chces odstranit? ")
    if delete in letters:
        letters.remove(delete)
        print(letters)
    else:
        print("Pismeno neni v seznamu")
print("seznam je prazdny")


        

    
