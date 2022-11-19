from abc import abstractmethod
from typing import Tuple

from Camera import Camera


class Drawable:

    def __init__(self, window, camera: Camera):
        self.window = window
        self.camera = camera

    @abstractmethod
    def get_pos(self) -> Tuple[float, float]:
        pass

    @abstractmethod
    def get_size(self) -> Tuple[float, float]:
        pass

    def get_right_bottom_pos(self) -> Tuple[float, float]:
        return tuple(pos + size for (pos, size) in zip(self.get_pos(), self.get_size()))

    def get_center(self) -> Tuple[float, float]:
        return tuple(pos + size/2 for (pos, size) in zip(self.get_pos(), self.get_size()))


    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def draw_on_pos(self, pos: Tuple[float, float]):
        pass