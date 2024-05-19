"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jan Kašpárek
email: jan.kasparek96@gmail.com
discord: jankasparek0720
"""

def Login():
    login_name = input("Insert user name: ")
    login_password = input("Inser password: " )

    user_name = ["bob", "ann", "mike", "liz"]
    passwords = ["123", "pass123", "password123", "pass1123"]
    '''
    if (login_name in user_name):
        bob = user_name[0] == login_name and passwords[0] == login_password
        ann = user_name[1] == login_name and passwords[1] == login_password
        mike = user_name[2] == login_name and passwords[2] == login_password
        liz = user_name[3] == login_name and passwords[3] == login_password
    
        if bob or ann or mike or liz:
            print("Welcome to the app,", login_name ,"\nWe have 3 texts to be analyzed.")
        else:
            print("Unregistered user, terminating the program..")
            quit()
    else:
        print("Unregistered user, terminating the program..")
        quit()
    '''

    if (login_name in user_name): #and (login_password in passwords):

        for i in user_name:
            if i == login_name:
                user_name.index(i)
                break
        
        for x in passwords:
            if x == login_password:
                passwords.index(x)
                break    

        if user_name.index(i) == passwords.index(x):
            print("Welcome to the app,", login_name ,"\nWe have 3 texts to be analyzed.")
        else:
            print("wrong password, try again")
            Login()
            
    else:
        print("Unregistered user, terminating the program..")
        quit()
Login()

import task_template as task

text_number = input("Enter a number btw. 1 and 3 to select:")
