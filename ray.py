import numpy as np


class Ray:
    def __init__(self, origin, direction):
        self.origin = np.array(origin, dtype=float)

        direction = np.array(direction, dtype=float)
        self.direction = direction / np.linalg.norm(direction)

    def point_at(self, t):
        return self.origin + t * self.direction