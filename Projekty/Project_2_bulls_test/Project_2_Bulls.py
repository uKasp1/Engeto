import random
u_list = []
r_list = []

def Hello():
    print("Hi there!",
          50*"-",
          "I've generated a random 4 digit number for you.",
          "Let's play a bulls and cows game.",
           sep="\n")
    
def Random_number():
    global r_list
    for i in range(4):
        if i == 0:
            r_list.append(random.randrange(1,9))
        else:
            r_list.append(random.randrange(0,9))
    print(r_list)
    User_Input()


def User_Input():
    global u_list
    try:
        print(50*"-")
        user_number = int(input("Enter a number:"))
    except ValueError:
        print(50*"-", "This is not a number, try again ", sep="\n")
        User_Input()
    else:
        user_number = str(user_number)
        if len(user_number) != 4:
            print("This is not a required lenght of the input, try again")
            User_Input()

        for i in user_number:
            u_list.append(int(i))
        print(u_list)
        Check_number()
    
def Check_number():
    global u_list
    bulls = 0 
    cows = 0 
    cows1 = 0

    for i in range(4):
        if r_list[i] == u_list[i]:
            bulls += 1
        for j in range(4):
            if r_list[i] == u_list[j]:
                cows += 1 
                cows1 += 1
    

    print(bulls, "Bulls,", cows - bulls, "Cows")

    if  bulls != 4:
        u_list = []
        User_Input()
    else:
        print("You won")
        




Hello()  
Random_number()
