import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
    
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_move())

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        while True:
            square = input("Move to: ")
            try:
                value = int(square)
                if value not in game.available_move():
                    raise ValueError
                return value
            except ValueError:
                print(f"Invalid move, please input again, the available move are: {game.available_move()}")

class GeniusComputerPlayer(Player):
    ...
