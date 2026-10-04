import numpy as np

#mirror 
def mirror(direction, normal):
    R = direction - 2 * np.dot(direction, normal) * normal
    return R


#lambertian material
def lambertian(normal):
    return 