logo ="""  _____ _    _ ______  _____ _____   _______ _    _ ______   _   _ _    _ __  __ ____  ______ _____  
  / ____| |  | |  ____|/ ____/ ____| |__   __| |  | |  ____| | \ | | |  | |  \/  |  _ \|  ____|  __ \ 
 | |  __| |  | | |__  | (___| (___      | |  | |__| | |__    |  \| | |  | | \  / | |_) | |__  | |__) |
 | | |_ | |  | |  __|  \___ \\___ \     | |  |  __  |  __|   | . ` | |  | | |\/| |  _ <|  __| |  _  / 
 | |__| | |__| | |____ ____) |___) |    | |  | |  | | |____  | |\  | |__| | |  | | |_) | |____| | \ \ 
  \_____|\____/|______|_____/_____/     |_|  |_|  |_|______| |_| \_|\____/|_|  |_|____/|______|_|  \_\
                                                                                                      
                                                                                                      """
print(logo)
print(f"Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between 1 and 100.")

"""
import random
x=[]
for i in range (1,101):
    x.append(i)
#print(x)
a=random.choice(x)
c=5
d=10
b=input(f"Choose a difficulty. Type 'easy' or 'hard':")
if b=="easy":
    while d:
        f=int(input(f"You have {d} attempts remaining to guess the number.\nMake a guess:"))
        if a>f:
            print("Too low.")
            d-=1
        elif a<f:
            print("Too high.")
            d-=1
        elif a==f:
            print(f"You got it! The answer was {a}.")
            break
    if d==0:
        print(f"You've run out of guesses, you lose.")
        print(f"try again!!!\nNEXT TIME")
    
            
    
            
elif b=="hard":
    while c:
        f=int(input(f"You have {c} attempts remaining to guess the number.\nMake a guess:"))
        if a>f:
            print("Too low.")
            c-=1
        elif a<f:
            print("Too high.")
            c-=1
        elif a==f:
            print(f"You got it! The answer was {a}.")
            break
    if c==0:
        print(f"You've run out of guesses, you lose.")
        print(f"try again!!!\nNEXT TIME")
        
else:
    print(f"Wrong!!! Please  Type 'easy' or 'hard' only")
    print(f"try again!!!\nNEXT TIME")
"""
import random
x=[]
for i in range (1,101):
    x.append(i)
#print(x)
a=random.choice(x)
c=5
d=10
def easy():
    global d
    while d:
        f=int(input(f"You have {d} attempts remaining to guess the number.\nMake a guess:"))
        if a>f:
            print("Too low.\nGuess Again")
            d-=1
        elif a<f:
            print("Too high.\nGuess Again")
            d-=1
        elif a==f:
            print(f"You got it! The answer was {a}.")
            break
    if d==0:
        print(f"You've run out of guesses, you lose.")
        print(f"try again!!!\nNEXT TIME")
def hard():
    global c
    while c:
        f=int(input(f"You have {c} attempts remaining to guess the number.\nMake a guess:"))
        if a>f:
            print("Too low.\nGuess Again")
            c-=1
        elif a<f:
            print("Too high.\nGuess Again")
            c-=1
        elif a==f:
            print(f"You got it! The answer was {a}.")
            break
    if c==0:
        print(f"You've run out of guesses, you lose.")
        print(f"try again!!!\nNEXT TIME")
    
#main
b=input(f"Choose a difficulty. Type 'easy' or 'hard':")
if b=="easy":
    easy()
elif b=="hard":
    hard()
else:
    print(f"Wrong!!! Please  Type 'easy' or 'hard' only")
    print(f"try again!!!\nNEXT TIME")



