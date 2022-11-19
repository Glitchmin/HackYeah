from copy import copy
from typing import List, Tuple

from BuildingElement import BuildingElement


class Builder:

    def __init__(self, budget: int, grid_size: int, elements_choice: List[BuildingElement]):
        self.budget = budget
        self.grid_size = grid_size
        self.elements_choice = elements_choice
        self.selected = copy(elements_choice[0])

    def show_selected(self, pos: Tuple[float, float]):
        if self.selected is not None:
            self.selected.physical.body.position = pos
            self.selected.physical.draw()

    # def build(self, pos: Tuple[float, float]):
    #     pos = (pos)