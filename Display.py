from GameObjects import Board
import os


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Display:
    def __init__(self, board: Board):
        self.board = board

    def refresh_screen(self):
        os.system("cls")
        index = 99
        for i in range(0, 10):
            for j in range(0, 11):
                if j < 10:
                    space = " "
                    pixel = str(self.board.boxes[index])
                    print(BColors.OKBLUE + pixel + (space * (5 - len(pixel))), end=" ")
                    index -= 1
                elif j is 10 and i < len(self.board.stats):
                    print(f"{BColors.OKGREEN}{list(self.board.stats[i].keys())[0]}", self.board.stats[i][list(self.board.stats[i].keys())[0]], end=" ")
            if index is not -1:
                print("\n")
            else:
                print(" <=========== START \n")
        print(f"{BColors.FAIL}LADDER ENCOUNTERED LIST:[", end=" ")
        for ladder in self.board.stats[1]["LADDER_NAMES"]:
            print(ladder, end=" ")
        print("]")
        print(f"{BColors.FAIL}SNAKES ENCOUNTERED LIST:[", end=" ")
        for snake in self.board.stats[2]["SNAKE_NAMES"]:
            print(snake, end=" ")
        print("]")

