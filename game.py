import json
import random
from string import capwords


def home():
    print("***Welcome To Guessing Game***")
    print("\n")
    w=int(input("***Press 1 To See Rules/Guide*** -->"))
    print("\n")

    if w==1:
        print("\n")
        print("*** Rules/Guide For The Game >_< ***")
        print("1.The computer chooses a number from 1 to 100")
        print("2.You will get 10/5/3 chances to guess the number")
        print("5.The game is  with three modes of difficultly")
        print("*** Good luck there Sherlock Homes ;) ***")
        print("\n")
        p=int(input("Press 1 To continue the game -->"))

        if p==1:
            mode()

def mode():
    print("***select your difficultly***")
    print("\n")
    print("Easy(10 try)   --> Press E")
    print("Medium(5 try) --> Press M")
    print("Hard(3 try)   --> Press H")
    print("Exit   --> Press 0")
    print("\n")
    p=input("Enter here -->")
    if capwords(p)=='E':
        easy_game()

    elif capwords(p)=='M':
        mid_game()

    elif capwords(p)=='H':
        hard_game()

    elif p=='0':
        home()


    else:
        print("\n")
        print("***Error. try again***")
        print("\n")
        mode()

def exit_app():
    p=input("Type X to main menu "
            "Type O to new game: ")
    if capwords(p)=='X':
        home()
    elif capwords(p)=='O':
        mode()

def easy_game():
    x = random.randint(1,100)
    y = int(input("Enter your first guess (1 to 100): "))
    for i in range(1,11):
        if x==y:
            if i==1:
                print("Correct. attempt 1")
                exit_app()
            elif i==2:
                print("Correct. attempt 2")
            elif i==3:
                print("Correct. attempt 3")
            elif i==4:
                print("Correct. attempt 4")
            elif i==5:
                print("Correct. attempt 5")
            elif i==6:
                print("Correct. attempt 6")
            elif i==7:
                print("Correct. attempt 7")
            elif i==8:
                print("Correct. attempt 8")
            elif i == 9:
                print("Correct. attempt 9")
            elif i==10:
                print("Correct. attempt 10")

            exit_app()
            return



        elif i<10:
            if x>y:
                y=int(input("Higher. Try again: "))
            elif x<y:
                y=int(input("Lower. Try again: "))

    print("***You lose***")
    print("Number was ", x)
    exit_app()





def mid_game():
    x = random.randint(1, 100)
    y = int(input("Enter your first guess (1 to 100): "))
    for i in range(1,6):
        if x==y:
            if i==1:
                print("Correct. attempt 1")
                exit_app()
            elif i==2:
                print("Correct. attempt 2")
            elif i==3:
                print("Correct. attempt 3")
            elif i==4:
                print("Correct. attempt 4")
            elif i==5:
                print("Correct. attempt 5")
            exit_app()
            return



        elif i < 5:
            if x > y:
                y = int(input("Higher. Try again: "))
            elif x < y:
                y = int(input("Lower. Try again: "))

    print("***You lose***")
    print("Number was ", x)
    exit_app()

def hard_game():
    x = random.randint(1, 100)
    y = int(input("Enter your first guess (1 to 100): "))
    for i in range(1, 4):
        if x == y:
            if i == 1:
                print("Correct. attempt 1")
                exit_app()
            elif i == 2:
                print("Correct. attempt 2")
            elif i == 3:
                print("Correct. attempt 3")


            exit_app()
            return



        elif i < 3:
            if x > y:
                y = int(input("Higher. Try again: "))
            elif x < y:
                y = int(input("Lower. Try again: "))

    print("***You lose***")
    print("Number was ", x)
    exit_app()





if __name__ == '__main__':
    home()