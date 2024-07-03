"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jan Kašpárek
email: jan.kasparek96@gmail.com
discord: jankasparek0720
"""
# import the task_template.py (needs to be in poject folder) as task 
import task_template as task

#Credentials input
users = {0:
            {"name":"bob",
            "password":"123"},
        1:
            {"name":"ann",
            "password":"pass123"},
        2:
            {"name":"mike",
            "password":"password123"},
        3:
            {"name":"liz",
            "password":"pass123"},
        }
    
index = 1             
while index == 1:

    login_name = input("\nInsert user name: ")
    login_password = input("Inser password: " )

    for i in users:
        if login_name == users[i]["name"] and login_password == users[i]["password"]:
            print("*"*40)
            print("Welcome to the app,", login_name ,"\nWe have 3 texts to be analyzed.")
            print("*"*40)
            index = 0
            break

        elif login_name == users[i]["name"] and login_password != users[i]["password"]:
            print("*"*25)
            print("wrong password, try again")
            print("*"*25)
            break

        else:
            continue
    else:
        print("*"*44)
        print("Unregistered user, terminating the program..")
        print("*"*44)
        quit()   

def text_analyze():   
#Coded in Try/Exept condition if input is not text
    try:
        text_number = int(input("Enter a number btw. 1 and 3 to select: "))
        print("You choose text n.",text_number)
        print("*"*40) 

    #Allow only 1 - 3 input 
        if text_number >= 1 and text_number <= len(task.TEXTS):
        #Take the specific text from tuple in task 
            chosen_text = task.TEXTS[text_number - 1] # -1 because tuple index starts from 0 

        #Number of words 
        #Takes the whole text and splits it to separate words
            split_of_words = chosen_text.split()
            number_of_words = len(split_of_words)
            print("There are",number_of_words ,"words in the selected text")

        #Titlecase words
            a = 0
        #Uppercase words
            b = 0
        #Lowercase words
            c = 0
        #Numeric words
            d = 0
            sum = 0
        #list for cleared words  
            clear_words = list()
        #dict for lenght of words and their numbers
            lenght_words = {}
        #Special symbols to be removed 
            symbols = [",",".","?","!","@","#","$","%","&","/","|"]

            for i in split_of_words: 
                
            #Titlecase words
                tittlecase = str(i)
                if tittlecase[0].isupper():
                    a=a+1 
                else:
                    a=a+0  

            #Uppercase words
                uppercase = str(i)
                if uppercase.isupper() and not uppercase[0].isdigit(): #exlude uppercase words with digits in it 
                    b=b+1 
                else:
                    b=b+0
        
            #Lowercase words
                lowercase = str(i)
                if lowercase.islower() and not lowercase[0].isdigit():# Exclude lovercase words with digits in it
                    c=c+1 
                else:
                    c=c+0

            #Numeric words
                digit = str(i)
                if digit.isnumeric():
                    d=d+1 
                    sum = sum+int(i)
                else:
                    d=d+0
            
            # Block for remowing special symbols from letters 
                for j in symbols:
            #take each word from split words and removes symbol
                    i = i.replace(j,"")
            #Cleared words insert into list     
                clear_words.append(i)


            print("There are",a ,"titlecase words.")
            print("There are",b ,"uppercase words.")
            print("There are",c ,"lowercase words.")
            print("There are",d ,"numeric strings.")
            print("The sum of all the numbers ", sum)

    # Wrong input closure of program 
        else:
            print("Wrong selection of text, terminating the program..")
            quit()
        
    #Block of code which puts lenght of cleared words and their count into a dict 
        for i in clear_words:
            lenght = len(i)
            if lenght not in lenght_words:
                lenght_words[lenght] = 1
            else:
                lenght_words[lenght] = lenght_words[lenght] + 1

    #printing of the results
        print("*"*33)
        print("LEN|{:^23}|NR".format("OCCURENCES"))      
        for i in sorted(lenght_words):
            print(f"{i:3}|{lenght_words[i]*"*":23}|{lenght_words[i]}")
        print("*"*49)

    #user has chance to start program once again 
        repeat = input("Do you wanna analyzed different text?(Yes/No):")
        repeat = repeat.lower()
        print("*"*49)

    #take only yes/no as answer else quit 
        if repeat == "yes":
            text_analyze()
        elif repeat == "no":
            print("Ok, Bye")
            print("*"*49)
            quit()
        else:
            print("Dont understand, terminating the program..")
            print("*"*49)
            quit()
#Exept error it will pop up error msg that input type is not a number for text number
    except ValueError as e:
        print("*"*40)
        print("This is not a number, terminating the program..")
        print("*"*40)    
        
text_analyze()
