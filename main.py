from ray import Ray
from object import Sphere 
from materials import mirror, lambertian
import numpy as np



ray = Ray(
    [0, 0, 0],
    [0, 0, -1]
)

sphere = Sphere(
    [0, 0, -3],
    1)

t = sphere.intersect(ray)
print(t)

if t is not None:
    hit_point = ray.origin + t * ray.direction

    normal = sphere.normal_at(hit_point)

    print("t:", t)
    print("hit point:", hit_point)
    print("normal:", normal)

    reflected = mirror(ray.direction, normal)

    print(reflected)




print("nflkenflkewnfklendlfnj")

normal = np.array([0.0, 0.0, 1.0])
direction = lambertian(normal)
print(direction)
print(np.dot(direction, normal))