import numpy as np


#mirror 
def mirror(direction, normal):
    R = direction - 2 * np.dot(direction, normal) * normal
    return R


#lambertian material
def lambertian(normal):
    rx = np.random.random()
    ry = np.random.random()
    vec = [num1, num2]
    r = sqrt(rx)
    theta = 2*np.pi*ry

    x = r*np.cos(theta)
    y = r*np.sin(theta)
    z = sqrt(1-rx)

    #rotate to the right direction

    local_direction = np.array([x, y, z])



     
    return 