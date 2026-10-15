
import numpy as np
import math as math
import numpy as np
from object import Polygon

class circLightSource:
    def __init__(self, x, y, z, radius=1.0, num_rays=200):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.num_rays = num_rays

    def generate_rays(self):
        rays = []

        # Uniformly distribute points on a sphere
        for i in range(self.num_rays):
            
            # go from z = 1 to z = -1
            z_dir = 1 - 2 * (i + 0.5) / self.num_rays
            phi = np.pi * (3 - np.sqrt(5)) * i

            r_xy = np.sqrt(1 - z_dir**2)

            dx = r_xy * np.cos(phi)
            dy = r_xy * np.sin(phi)
            dz = z_dir

            # Starting point on the sphere's surface
            start_x = self.x + self.radius * dx
            start_y = self.y + self.radius * dy
            start_z = self.z + self.radius * dz

            rays.append({
                "origin": (start_x, start_y, start_z),
                "direction": (dx, dy, dz)
            })

        return rays


class boxLightSource:
    # x, y - positions, radius e size, numray e number of rays
    def __init__(self, x, y, z, width, num_rays=40): # num rays is per face for now
        self.x = x
        self.y = y
        self.z = z
        # start with size implement different dimensions later for ease
        self.size = width
        self.num_rays = num_rays

    def generate_rays(self):
        # points for each face
        points = np.linspace(
            -self.size / 2,
            self.size / 2,
            self.num_rays
        )

        rays = []

        for a in points:
            for b in points:

                # +X face
                rays.append({
                    "origin": (self.x + self.size/2,
                               self.y + a, self.z + b),
                    "direction": (1, 0, 0)
                })

                # -X face
                rays.append({
                    "origin": (self.x - self.size/2,
                               self.y + a, self.z + b),
                    "direction": (-1, 0, 0)
                })

                # +Y face
                rays.append({
                    "origin": (self.x + a,
                               self.y + self.size/2, self.z + b),
                    "direction": (0, 1, 0)
                })

                # -Y face
                rays.append({
                    "origin": (self.x + a,
                               self.y - self.size/2, self.z + b),
                    "direction": (0, -1, 0)
                })

                # +Z face
                rays.append({
                    "origin": (self.x + a, self.y + b,
                               self.z + self.size/2),
                    "direction": (0, 0, 1)
                })

                # -Z face
                rays.append({
                    "origin": (self.x + a, self.y + b,
                               self.z - self.size/2),
                    "direction": (0, 0, -1)
                })

        return rays


# För att testa randomness i ray distribution !!!
# currently not different
class circLightSource2:
    def __init__(self, x, y, z, radius=1.0, num_rays=200):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.num_rays = num_rays

    def generate_rays(self):
        rays = []

        # Uniformly distribute points on a sphere
        for i in range(self.num_rays):
            
            # go from z = 1 to z = -1
            z_dir = 1 - 2 * (i + 0.5) / self.num_rays
            phi = np.pi * (3 - np.sqrt(5)) * i

            r_xy = np.sqrt(1 - z_dir**2)

            dx = r_xy * np.cos(phi)
            dy = r_xy * np.sin(phi)
            dz = z_dir

            # Starting point on the sphere's surface
            start_x = self.x + self.radius * dx
            start_y = self.y + self.radius * dy
            start_z = self.z + self.radius * dz

            rays.append({
                "origin": (start_x, start_y, start_z),
                "direction": (dx, dy, dz)
            })

        return rays

# working on it
class boxLightSource2:
    # x, y - positions, radius e size, numray e number of rays
    def __init__(self, x, y, z, width, num_rays=40): # num rays is per face for now (kan behöva increase it a lot)
        self.x = x
        self.y = y
        self.z = z
        # start with size implement different dimensions later for ease
        self.size = width
        self.num_rays = num_rays

    def generate_rays(self):
        # points for each face
        points = np.linspace(
            -self.size / 2,
            self.size / 2,
            self.num_rays
        )

        rays = []

        # random nr between -1 and 1
        # -1 + 2 * np.random.random(1)

        for a in points:
            for b in points:

                # try this but everywhere
                # +X face
                rays.append({
                    "origin": (self.x + self.size/2,
                               self.y + a, self.z + b),
                    "direction": (1, -1 + 2 * np.random.random(1), -1 + 2 * np.random.random(1))
                })

                # -X face
                rays.append({
                    "origin": (self.x - self.size/2,
                               self.y + a, self.z + b),
                    "direction": (-1, -1 + 2 * np.random.random(1), -1 + 2 * np.random.random(1))
                })

                # +Y face
                rays.append({
                    "origin": (self.x + a,
                               self.y + self.size/2, self.z + b),
                    "direction": (0, 1, 0)
                })

                # -Y face
                rays.append({
                    "origin": (self.x + a,
                               self.y - self.size/2, self.z + b),
                    "direction": (0, -1, 0)
                })

                # +Z face
                rays.append({
                    "origin": (self.x + a, self.y + b,
                               self.z + self.size/2),
                    "direction": (0, 0, 1)
                })

                # -Z face
                rays.append({
                    "origin": (self.x + a, self.y + b,
                               self.z - self.size/2),
                    "direction": (0, 0, -1)
                })

        return rays

