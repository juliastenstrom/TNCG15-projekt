import numpy as np
from ray import Ray

class Sphere:
    #how a sphere is defined
    def __init__(self, center, radius):
        self.center = np.array(center, dtype=float)
        self.radius = radius

    #how many rays actually hit the sphere
    def intersect(self, ray):

        #does the ray pass close enough to the sphere to hit it?
        L = self.center - ray.origin
        t = np.dot(L, ray.direction)
        d_square = np.dot(L, L) - t**2
        if d_square > self.radius**2:
            return None

        #find intersection distance
        th = np.sqrt(self.radius**2 - d_square)
        t0 = t - th
        t1 = t + th

        if t0 > 0:
            return t0

        if t1 > 0:
            return t1

        return None

    #find normal is needed for materials later
    def normal_at(self, point):
        P = point
        C = self.center
        N = P - C
        N = N/np.linalg.norm(N)

        return N

