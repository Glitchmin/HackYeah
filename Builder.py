from copy import copy, deepcopy
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
            self.selected.physical.body.position = self.pos_in_grid(pos)
            self.selected.physical.draw()

    def build(self, pos: Tuple[float, float]):
        if self.selected is not None:
            pos = self.pos_in_grid(pos)
            new_element = self.selected.physical.copy()
            new_element.body.position = pos
            return new_element
        else:
            return None

    def pos_in_grid(self, pos):
        return (pos[0] - pos[0] % self.grid_size, pos[1] - pos[1] % self.grid_size)