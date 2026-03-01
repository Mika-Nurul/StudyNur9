import numpy as np
import math as m

def angle_between(u, v):
    u = np.array(u)
    v = np.array(v)
    pr = np.dot(u, v)
    mod_u = np.linalg.norm(u)
    mod_v = np.linalg.norm(v)
    cos_angle = pr / (mod_u * mod_v)
    return np.degrees(m.acos(cos_angle))
spis = [[1,0],[0,1],[-1,0],[0,-1]]
def ortv(spis):
    for u in spis:
        for v in spis:
            if angle_between(u,v) == 90 or angle_between(u,v) == 270:
                print(u,v)
print(ortv(spis))
