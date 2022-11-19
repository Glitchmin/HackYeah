from typing import Tuple



class Camera:

    def __init__(self, size: Tuple[int, int], pos: Tuple[float, float] = (0, 0)):
        self.target = None
        self.pos = pos
        pass

    def set_pos(self, pos: Tuple[float, float]):
        pass

    def set_center(self, pos: Tuple[float, float]):
        pass

    def follow(self, target):
        self.target = target

    def to_scr_pos(self, pos: Tuple[float, float]) -> Tuple[float, float]:
        if self.target is not None:
            self.set_center(self.target.get_pos())
        pass

