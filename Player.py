from Catapult import Catapult
from Game import Game


class Player:
    def __init__(self, isFirst: bool, game: Game):
        self.money: int = 100
        self.catapult: Catapult = None
        self.king = None
        self.isFirst: bool = isFirst
        self.game: Game = game

    def playerTurn(self):
        self.catapult = Catapult(self.game, self.isFirst)

