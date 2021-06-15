import mpl_toolkits
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import sp
import math
import sp
from sp import *

print("\n 1:Black_hole\n 2:normalmasses\n")
data = int(input("\n enter your choice:"))
if data == 1:
    G = 6.626 * pow(10,-11)
    solar_mass = 2 * math.pow(10, 30)
    c = 3 * math.pow(10, 8)
    m = float(input("\n enter the mass of blackhole in solar masses:"))
    radius = 2*m*G/(math.pow(c, 2))*2*math.pow(10,30)
    print(radius)
    volume = 4 / 3 * math.pi * math.pow(radius, 3)*pow(10,21)
    print(volume)
    sigma = (m * 2 *math.pow(10,30)/ (volume))
    n = int(sigma)
    R = radius


    def fun(x, y):
        if sigma != 0:
            return (-1 / sigma * math.sqrt(2 * math.pi) * np.exp(
                -1 / 2 * (np.power(x * sigma, 2) + np.power(y * sigma, 2))))


    x = np.arange(-10000, 10000, 10)
    y = np.arange(-10000, 10000, 10)
    X, Y = np.meshgrid(x, y)
    zs = np.array((fun(np.ravel(X), np.ravel(Y))))

    Z = zs.reshape(X.shape)
    sphere(R, n)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
    radius = radius/10**1
    m = radius*np.cos(u) * np.sin(v)
    l = radius*np.sin(u) * np.sin(v)
    k = radius*np.cos(v)


    ax.plot_surface(X, Y, Z, cmap="viridis")


    plt.show()

elif data == 2:
    m = float(input("\n Input the mass :"))
    radius = float(input("\n Input the radius:"))
    volume = 4 / 3 * math.pi * math.pow(radius, 3)
    sigma = m / volume
    n = int(sigma)
    R = radius


    def fun(x, y):
        if sigma != 0:
            return (-1 / sigma * math.sqrt(2 * math.pi) * np.exp(
                -1 / 2 * (np.power(x * sigma, 2) + np.power(y * sigma, 2))))


    x = np.arange(-1000, 1000, 10)
    y = np.arange(-1000, 1000, 10)
    X, Y = np.meshgrid(x, y)
    zs = np.array((fun(np.ravel(X), np.ravel(Y))))

    Z = zs.reshape(X.shape)
    sphere(R, n)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
    m = 10*radius* np.cos(u) * np.sin(v)
    l = 10*radius *np.sin(u) * np.sin(v)
    k = 10*radius *np.cos(v)

    ax.plot_surface(X, Y, Z, cmap='viridis')
    


    plt.show()




