from random import randint
import sys


class SnakeLadder:
    def __init__(self, b, e, serial_no):
        self.tuple_ladder = (b, e)
        self.b = b
        self.e = e
        self.serial_no = serial_no
        self.type = {True: "S:", False: "L:"}[b > e]

    def __str__(self):
        return f"{self.type}{self.serial_no}({self.tuple_ladder[0] + 1}->{self.tuple_ladder[1] + 1})"

    def __repr__(self):
        return f"{self.type}{self.serial_no}({self.tuple_ladder[0] + 1}->{self.tuple_ladder[1] + 1})"


class Board:
    def __init__(self):
        self.boxes = [i for i in range(1, 101)]
        self.snakes = {}
        self.ladders = {}
        self.current_player_box = -1
        self.verified = False
        self.no = 1
        self.display = None
        self.game_over = False
        self.stats = [
            {"DICE_THROWN": 0},
            {"LADDERS_CLIMBED": 0, "LADDER_NAMES": []},
            {"SNAKES_ENCOUNTERED": 0, "SNAKE_NAMES": []}
        ]

    def set_display(self, display):
        self.display = display

    def set_snakes(self, snakes, refresh=False):
        from Display import BColors
        if refresh:
            for snake in self.snakes:
                snake_obj = self.snakes[snake]
                self.boxes[snake_obj.b] = f"{BColors.FAIL}SB{snake_obj.serial_no}  "
                self.boxes[snake_obj.e] = f"{BColors.FAIL}SE{snake_obj.serial_no}  "
            return
        for snake in snakes:
            try:
                self.snakes[str(snake.b)]
                raise Exception("No two snakes can have same beginning.")
            except KeyError:
                self.snakes[str(snake.b)] = snake
                self.boxes[snake.b] = f"{BColors.FAIL}SB{snake.serial_no}  "
                self.boxes[snake.e] = f"{BColors.FAIL}SE{snake.serial_no}  "

    def set_ladders(self, ladders, refresh=False):
        from Display import BColors
        if refresh:
            for ladder in self.ladders:
                ladder_obj = self.ladders[ladder]
                self.boxes[ladder_obj.b] = f"{BColors.OKGREEN}LB{ladder_obj.serial_no}  "
                self.boxes[ladder_obj.e] = f"{BColors.OKGREEN}LE{ladder_obj.serial_no}  "
            return
        for ladder in ladders:
            try:
                self.ladders[str(ladder.b)]
                raise Exception("No two ladders can have same beginning.")
            except KeyError:
                self.ladders[str(ladder.b)] = ladder
                self.boxes[ladder.b] = f"{BColors.OKGREEN}LB{ladder.serial_no}  "
                self.boxes[ladder.e] = f"{BColors.OKGREEN}LE{ladder.serial_no}  "

    def verify(self):
        for key in self.snakes.keys():
            if key in self.ladders.keys():
                raise Exception("Beginning of Snake and Ladder cannot be same.")
        self.verified = True
        return True

    @staticmethod
    def throw_dice():
        return randint(1, 6)

    def play(self):
        if not self.verified:
            raise Exception("Snakes and ladders need to ve verified first")
        if self.game_over:
            self.boxes[99] = "[ GAMEOVER ]"
            self.display.refresh_screen()
            print("GAME OVER: YOU HAVE COMPLETED THE GAME. Please restart the game. Press any key to continue")
            input()
            return
        self.stats[0]["DICE_THROWN"] += 1
        dice_value = Board.throw_dice()
        key = str(self.current_player_box + dice_value)
        if self.current_player_box is not -1:
            self.boxes[self.current_player_box] = self.no
        if str(key) in self.snakes.keys():
            snake = self.snakes[str(key)]
            self.current_player_box = snake.e
            self.stats[2]["SNAKES_ENCOUNTERED"] += 1
            self.stats[2]["SNAKE_NAMES"].append(str(snake))
        elif str(key) in self.ladders.keys():
            ladder = self.ladders[str(key)]
            self.current_player_box = ladder.e
            self.stats[1]["LADDERS_CLIMBED"] += 1
            self.stats[1]["LADDER_NAMES"].append(str(ladder))
        else:
            self.current_player_box = int(key)
        if self.current_player_box > 98:
            self.current_player_box = 99
            self.no = self.boxes[self.current_player_box] = "[ GAMEOVER ]"
            self.display.refresh_screen()
            print(f"\nValue on dice is:[{dice_value}]")
            print("GAME OVER: YOU HAVE COMPLETED THE GAME. Press any key to continue")
            input()
            self.game_over = True
        else:
            from Display import BColors
            self.no = self.boxes[self.current_player_box]
            self.boxes[self.current_player_box] = f"{BColors.WARNING}(@@)"
            self.display.refresh_screen()
        print(f"\nValue on dice is:[{dice_value}]")

    def start(self):
        if not self.display:
            raise Exception("Display has not been set.")
        while True:
            try:
                if self.game_over:
                    print("\n You have completed the game.Please enter 1 to restart the game or"
                          " type exit to exit from game")
                else:
                    print("\nEnter t to throw the dice, Enter 1 to restart the game, type exit to exit from game")
                {
                    "t": lambda: self.play(),
                    "exit": lambda: sys.exit(0),
                    "1": self.refresh_game
                }[input()]()
            except KeyError:
                print("WRONG CHOICE. PLEASE TRY AGAIN")

    def refresh_game(self):
        self.boxes = [i for i in range(1, 101)]
        self.game_over = False
        self.set_snakes(None, True)
        self.set_ladders(None, True)
        self.stats = [
            {"DICE_THROWN": 0},
            {"LADDERS_CLIMBED": 0, "LADDER_NAMES": []},
            {"SNAKES_ENCOUNTERED": 0, "SNAKE_NAMES": []}
        ]
        self.current_player_box = -1
        self.no = 1
        self.display.refresh_screen()
