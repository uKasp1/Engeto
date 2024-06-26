"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jan Kašpárek
email: jan.kasparek96@gmail.com
discord: jankasparek0720
"""
# Start of the program  
def start():
    # Login to the program
    def Login():
        users = {1:
                 {"name":"bob",
                  "password":"123"},
                2:
                 {"name":"ann",
                  "password":"pass123"},
                3:
                 {"name":"mike",
                  "password":"password123"},
                4:
                 {"name":"liz",
                  "password":"pass123"},
                }
              
        login_name = input("\nInsert user name: ")
        login_password = input("Inser password: " )
        
        for i in users:
            if login_name == users[i]["name"] and login_password == users[i]["password"]:
                print("*"*40)
                print("Welcome to the app,", login_name ,"\nWe have 3 texts to be analyzed.")
                print("*"*40)
            elif login_name == users[i]["name"] and login_password != users[i]["password"]:
                print("*"*25)
                print("wrong password, try again")
                print("*"*25)
                Login()
            else:
                print("*"*44)
                print("Unregistered user, terminating the program..")
                print("*"*44)
                quit()
    Login()

    # import the task_template.py (needs to be in poject folder) as task 
    import task_template as task

    #Coded in Try/Exept condition if input is not text
    try:
        text_number = int(input("Enter a number btw. 1 and 3 to select: "))
        print("You choose text n.",text_number)
        print("*"*40) 

            # allow only 1 - 3 input 
        if text_number >= 1 and text_number <= 3:
            # Take the specific text from tuple in task 
            chosen_text = task.TEXTS[text_number - 1] # -1 because tuple index starts from 0 

            #Number of words 
            # Takes the whole text and splits it to separate words
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
                if uppercase.isupper() and not uppercase[0].isdigit(): #exlude uppercase words with digits in it 
                    b=b+1 
                else:
                    b=b+0
            print("There are",b ,"uppercase words.")

            #Lowercase words
            c = 0
            for i in split_of_words:
                lowercase = str(i)
                if lowercase.islower() and not lowercase[0].isdigit():# Exclude lovercase words with digits in it
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
        # Wrong input closure of program 
        else:
            print("Wrong selection of text, terminating the program..")
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
        # Takes every word separatly and will count its lenght
        for j in split_of_words:
            # from is removed , and . symbols
            j = j.replace(",","")   
            j = j.replace(".","")

            # compares how many characters the world have and count it up to the final value  
            if len(j) == 1:
                words1 = words1 + 1 
            elif len(j) == 2:
                words2 = words2 + 1
            elif len(j) == 3:
                words3 = words3 + 1
            elif len(j) == 4:
                words4 = words4 + 1
            elif len(j) == 5:
                words5 = words5 + 1
            elif len(j) == 6:
                words6 = words6 + 1
            elif len(j) == 7:
                words7 = words7 + 1
            elif len(j) == 8:
                words8 = words8 + 1
            elif len(j) == 9:
                words9 = words9 + 1
            elif len(j) == 10:
                words10 = words10 + 1
            elif len(j) == 11:
                words11 = words11 + 1
        # formating of the output texts
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
        # Its possible to repeat the program if user chosses 
        print("*"*49)
        repeat = input("Do you wanna analyzed different text?(Yes/No):")
        repeat = repeat.lower()
        print("*"*49)

        if repeat == "yes":
            start()
        elif repeat == "no":
            print("Ok, Bye")
            print("*"*49)
            quit()
        else:
            print("Dont understand, terminating the program..")
            print("*"*49)
            quit()

    # Insted of error it will pop up error msg that input type is not a number
    except ValueError as e:
        print("*"*40)
        print("This is not a number, terminating the program..")
        print("*"*40)    
start()