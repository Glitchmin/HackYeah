from Catapult import Catapult


class Player:
    def __init__(self, isFirst: bool, game):
        self.money: int = 100
        self.catapult: Catapult = None
        self.king = None
        self.isFirst: bool = isFirst
        self.game = game

    def playerTurn(self):
        self.catapult = Catapult(self.game, self.isFirst)
        self.game.drawables.append(self.catapult)
