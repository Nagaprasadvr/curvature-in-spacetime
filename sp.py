import random
from random import *
import math

import numpy as np
import random
import math
from random_geometry_points.sphere import Sphere
import pandas as pd  # (version 1.0.0)
import plotly.express as px  # (version 4.7.0)


p = []
m = []
l = []
k = []



def sphere(R,n):
 for i in range(0, n):
    phi = random.random() *2*math.pi
    costheta = random.random()*randrange(-1,2)
    u = random.random()
    theta = math.acos(costheta)
    r = R * math.pow(u, 1/3)
    x = (r * math.sin(theta) * math.cos(phi))

    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(theta)

    m.append(x)
    l.append(y)
    k.append(z)
    return m,l,k





