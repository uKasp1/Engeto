import task_template as task

text_number = int(input("Enter a number btw. 1 and 3 to select: "))
print(text_number)

if text_number >= 1 and text_number <= 3:
    chosen_text = task.TEXTS[text_number - 1]

    #Number of words 
    split_of_words = chosen_text.split()
    number_of_words = len(split_of_words)
    print("There are",number_of_words ,"words in the selected text")

    #Titlecase words
    a = 0
    for i in split_of_words:
        tittlecase = str(i)
        if tittlecase[0].isupper():
            a=a+1 
        else:
            a=a+0 
    print("There are",a ,"titlecase words.")

    #Uppercase words
    b = 0
    for i in split_of_words:
        uppercase = str(i)
        if uppercase.isupper() and not uppercase[0].isdigit():
            b=b+1 
        else:
            b=b+0
    print("There are",b ,"uppercase words.")

    #Lowercase words
    c = 0
    for i in split_of_words:
        lowercase = str(i)
        if lowercase.islower() and not lowercase[0].isdigit():
            c=c+1 
        else:
            c=c+0
    print("There are",c ,"lowercase words.")

    #Numeric words
    d = 0
    sum = 0
    for i in split_of_words:
        digit = str(i)
        if digit.isnumeric():
            d=d+1 
            sum = sum+int(i)
        else:
            d=d+0
    print("There are",d ,"numeric strings.")
    print("The sum of all the numbers ", sum)

else:
    print("Wrong selection of text, program will quit")
    quit()


#Lenght of words in text 
words1 = 0
words2 = 0
words3 = 0
words4 = 0
words5 = 0
words6 = 0
words7 = 0
words8 = 0
words9 = 0
words10 = 0
words11 = 0

for j in split_of_words:
    k = j.replace(",","")
    l = k.replace(".","")

    if len(l) == 1:
        words1 = words1 + 1 
    elif len(l) == 2:
        words2 = words2 + 1
    elif len(l) == 3:
        words3 = words3 + 1
    elif len(l) == 4:
        words4 = words4 + 1
    elif len(l) == 5:
        words5 = words5 + 1
    elif len(l) == 6:
        words6 = words6 + 1
    elif len(l) == 7:
        words7 = words7 + 1
    elif len(l) == 8:
        words8 = words8 + 1
    elif len(l) == 9:
        words9 = words9 + 1
    elif len(l) == 10:
        words10 = words10 + 1
    elif len(l) == 11:
        words11 = words11 + 1

print("*"*33)
print("LEN|{:^23}|NR".format("OCCUENCES"))
print("*"*33)
print("  1|","*"*words1," "*(20 - words1),"| ",words1)
print("  2|","*"*words2," "*(20 - words2),"| ",words2)
print("  3|","*"*words3," "*(20 - words3),"| ",words3)
print("  4|","*"*words4," "*(20 - words4),"| ",words4)
print("  5|","*"*words5," "*(20 - words5),"| ",words5)
print("  6|","*"*words6," "*(20 - words6),"| ",words6)
print("  7|","*"*words7," "*(20 - words7),"| ",words7)
print("  8|","*"*words8," "*(20 - words8),"| ",words8)
print("  9|","*"*words9," "*(20 - words9),"| ",words9)
print(" 10|","*"*words10," "*(20- words10),"| ",words10)
print(" 11|","*"*words11," "*(20 - words11),"| ",words11)