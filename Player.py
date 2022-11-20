from typing import Tuple

from BuildingElement import BuildingElement
from Catapult import Catapult
from Rectangle import Rectangle
from tuple_as_vector import v_add, v_mul


class Player:
    BASE_OFFSET = (0, 300)

    def __init__(self, isFirst: bool, game, pos_center: Tuple[float, float]):
        self.isFirst: bool = isFirst
        self.game = game
        self.pos_center = pos_center
        self.money: int = 100
        self.catapult: Catapult = None
        self.king = BuildingElement(
                Rectangle(self.game.display, self.game.camera, pos_center, size=(game.GRID_SIZE * 4, game.GRID_SIZE * 6),
                          image_loader=self.game.image_loader,image_name="testgrass.png"),
                cost=100, hp=10)
        self.game.space.add(self.king.physical.shape, self.king.physical.body)
        game.drawables.append(self.king.physical)

    def playerTurn(self):
        self.catapult = Catapult(self.game, self.isFirst,
                                 v_add(self.pos_center, v_mul((self.turn_multiplier(), 1), Player.BASE_OFFSET)))
        self.game.drawables.append(self.catapult)

    def turn_multiplier(self):
        return 1 if self.isFirst else -1
