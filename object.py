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


class Polygon: # currently square?
    def __init__(self, vertices):
        self.vertices = vertices
        self.normal = self.calculate_normal()

    def calculate_normal(self):
        edge1 = self.vertices[1] - self.vertices[0]
        edge2 = self.vertices[2] - self.vertices[0]

        normal = np.cross(edge1, edge2)

        return normal / np.linalg.norm(normal)
    

class Cuboid:
    def __init__(self, position, width, height, depth):
        self.position = position
        self.width = width
        self.height = height
        self.depth = depth

        x, y, z = position

        # 8 vertices
        v0 = np.array([x, y, z])
        v1 = np.array([x + width, y, z])
        v2 = np.array([x + width, y + height, z])
        v3 = np.array([x, y + height, z])

        v4 = np.array([x, y, z + depth])
        v5 = np.array([x + width, y, z + depth])
        v6 = np.array([x + width, y + height, z + depth])
        v7 = np.array([x, y + height, z + depth])

        # 6 faces
        self.faces = [
            Polygon([v0, v1, v2, v3]),  # front
            Polygon([v4, v7, v6, v5]),   # back

            Polygon([v0, v4, v5, v1]),  # bottom
            Polygon([v3, v2, v6, v7]),   # top

            Polygon([v0, v3, v7, v4]), # left
            Polygon([v1, v5, v6, v2])   # right
        ]

    def __str__(self):
        return f"Cuboid with vertices: {self.faces}"
