from abc import abstractmethod
from typing import Tuple

from Camera import Camera


class Drawable:

    def __init__(self, window, camera: Camera):
        pass

    @abstractmethod
    def get_pos(self) -> Tuple[float, float]:
        pass

    def draw(self):
        pass
