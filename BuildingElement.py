from Physical import Physical


class BuildingElement:

    def __init__(self, physical: Physical, cost: int):
        self.physical = physical
        self.cost = cost
