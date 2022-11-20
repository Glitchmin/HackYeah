from Physical import Physical


class BuildingElement:

    def __init__(self, physical: Physical, cost: int, hp:int):
        self.physical = physical
        self.cost = cost
        self.hp = hp
