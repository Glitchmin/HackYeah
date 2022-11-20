from copy import copy, deepcopy
from typing import List, Tuple

from BuildingElement import BuildingElement
from Camera import Camera


class Builder:

    def __init__(self, budget: int, grid_size: int, elements_choice: List[BuildingElement], camera: Camera):
        self.budget = budget
        self.grid_size = grid_size
        self.elements_choice = elements_choice
        self.selected = copy(elements_choice[0])
        self.camera = camera
        self.body_to_item_dict = {}
        self.angle = 0.0

    def show_selected(self, pos: Tuple[float, float]):
        if self.selected is not None:
            # self.selected.physical.body.position = self.pos_in_grid(pos)
            self.selected.physical.body.position = self.pos_in_grid(self.camera.to_world_pos(pos))
            self.selected.physical.body.angle = self.angle
            self.selected.physical.draw()
            # self.selected.physical.draw_on_pos(pos)

    def build(self, pos: Tuple[float, float]):
        if self.selected is not None:
            org_pos = pos
            pos = self.camera.to_world_pos(pos)
            pos = self.pos_in_grid(pos)
            new_element = BuildingElement(self.selected.physical.copy(), 10, 5 * 1000000)
            new_element.physical.body.position = pos
            new_element.physical.body.angle = self.angle

            self.body_to_item_dict[id(new_element.physical.body)] = new_element
            return new_element
        else:
            return None



    def pos_in_grid(self, pos):
        return (pos[0] - pos[0] % self.grid_size, pos[1] - pos[1] % self.grid_size)
