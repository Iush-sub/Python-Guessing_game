import json
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

def easy_game():
    print("easy")

def mid_game():
    print("medium")

def hard_game():
    print("hard")





if __name__ == '__main__':
    home()