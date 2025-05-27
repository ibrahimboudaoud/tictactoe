from enum import Enum

class Player(Enum):
    EMPTY = " "
    X = "X"
    O = "O"

def main() -> None:
    question()



def question() -> None:
    ask = True
    while ask:
        play = input("Do you want to play Tic-Tac-Toe? ").lower().strip()
        if play == "yes":
            #play()
            print("Let's get started!")
            ask = False
        elif play == "no":
            print("Have a nice day!")
            ask = False
        else:
            print("Invalid input, please answer yes or no:")


def play() -> None:
    gameBoard = {1: Player.EMPTY, 2: Player.EMPTY,3: Player.EMPTY,
                 4:Player.EMPTY,5: Player.EMPTY,6: Player.EMPTY,
                 7: Player.EMPTY,8: Player.EMPTY,9: Player.EMPTY}
    while not (winner()):

def winner(gameBoard) -> bool:
    for i in range(0, 9, 3):
        if()

main()