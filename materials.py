import numpy as np


#mirror 
def mirror(direction, normal):
    R = direction - 2 * np.dot(direction, normal) * normal
    return R


#lambertian material
def lambertian(normal):
    rx = np.random.random()
    ry = np.random.random()
    r = np.sqrt(rx)
    theta = 2*np.pi*ry

    x = r*np.cos(theta)
    y = r*np.sin(theta)
    z = np.sqrt(1-rx)

    local_direction = np.array([x, y, z])

    if(abs(normal[0]) < 0.9):
        helper = np.array([1.0,0.0,0.0])
    else:
        helper = np.array([0.0,1.0,0.0])

    tangent = np.cross(helper, normal)
    tangent = tangent / np.linalg.norm(tangent)

    bitangent = np.cross(normal, tangent)

    world_direction = (x*tangent + y*bitangent + z *normal)
    world_direction = world_direction / np.linalg.norm(world_direction)


    



     
    return world_direction