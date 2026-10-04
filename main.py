from ray import Ray
from object import Sphere
from materials import mirror


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
