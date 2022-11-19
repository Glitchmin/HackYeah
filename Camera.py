from typing import Tuple
# from Drawable import Drawable


class Camera:

    def __init__(self, size: Tuple[int, int], pos: Tuple[float, float] = (0, 0)):
        self.target = None
        self.pos = pos
        self.width = size[0]
        self.height = size[1]

    def set_pos(self, pos: Tuple[float, float]):
        self.pos = pos

    def set_center(self, center: Tuple[float, float]):
        self.pos = (
            center[0] - self.width / 2,
            center[1] - self.height / 2
        )

    # def follow(self, target: Drawable):
    def follow(self, target):
        self.target = target

    def update_followed(self):
        if self.target is not None:
            self.set_center(self.target.get_pos())

    def to_scr_pos(self, pos: Tuple[float, float]) -> Tuple[float, float]:
        self.update_followed()
        return (
            pos[0] - self.pos[0],
            pos[1] - self.pos[1]
        )

    def to_world_pos(self, pos: Tuple[float, float]) -> Tuple[float, float]:
        self.update_followed()
        return (
            pos[0] + self.pos[0],
            pos[1] + self.pos[1]
        )