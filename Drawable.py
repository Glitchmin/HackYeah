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
    def draw(self):
        pass
