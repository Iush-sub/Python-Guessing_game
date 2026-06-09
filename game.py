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
        print("1.The computer chooses a number from given range")
        print("2.You will get 5 chances to guess the number")
        print("3.On guessing it in first try you will be rewarded 100 points")
        print("4.On second try you will get 50, on third 25, fourth 10 and at fifth you will get 5 ")
        print("5.The game is also multiplayer with three modes of difficultly")
        print("*** Good luck there Sherlock Homes ;) ***")
        print("\n")
        p=int(input("Press 1 To continue the game -->"))

        if p==1:
            mode()

def mode():
    print("***select your difficultly***")
    print("\n")
    print("Easy   --> Press E")
    print("Medium --> Press M")
    print("Hard   --> Press H")
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
    x = random.randint(1,10)
    y = int(input("Enter your first guess (1 to 10): "))
    for i in range(1,4):
        if x==y:
            if i==1:
                print("100 points. first try")
                exit_app()
            elif i==2:
                print("50 points. second try")
            elif i==3:
                print("25 points. third try")
            exit_app()
            return



        elif i<3:
            if x>y:
                y=int(input("Higher. Try again: "))
            elif x<y:
                y=int(input("Lower. Try again: "))

    print("***You lose***")
    print("Number was ", x)
    exit_app()





def mid_game():
    x = random.randint(1, 50)
    y = int(input("Enter your first guess (1 to 50): "))
    for i in range(1,7):
        if x == y:
            if i == 1:
                print("150 points. first try")
                exit_app()
            elif i == 2:
                print("100 points. second try")
            elif i == 3:
                print("50 points. third try")
            elif i == 4:
                print("25 points. fourth try")
            elif i== 5:
                print("10 points. fifth try")
            else:
                print("5 points. sixth try")
            exit_app()
            return



        elif i < 7:
            if x > y:
                y = int(input("Higher. Try again: "))
            elif x < y:
                y = int(input("Lower. Try again: "))

    print("***You lose***")
    print("Number was ", x)
    exit_app()

def hard_game():
    print("hard")





if __name__ == '__main__':
    home()