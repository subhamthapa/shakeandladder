from GameObjects import *
from Display import Display

gameboard = Board()
display = Display(gameboard)
gameboard.set_display(display)
ladders = [
    SnakeLadder(12, 50, 1),
    SnakeLadder(20, 30, 2),
    SnakeLadder(35, 60, 3),
    SnakeLadder(24, 80, 4),
    SnakeLadder(40, 70, 5),
    SnakeLadder(43, 70, 6),
    SnakeLadder(22, 70, 7),

]

snakes = [
    SnakeLadder(71, 10, 1),
    SnakeLadder(55, 10, 2),
    SnakeLadder(98, 17, 3),
    SnakeLadder(62, 24, 4),
    SnakeLadder(26, 10, 5),
    SnakeLadder(76, 13, 6),
    SnakeLadder(92, 53, 7),
    SnakeLadder(83, 23, 8),
    SnakeLadder(66, 27, 9),

]
gameboard.set_snakes(snakes)
gameboard.set_ladders(ladders)
display.refresh_screen()
gameboard.verify()
gameboard.start()
