
import numpy as np
import random as random
import matplotlib.pyplot as plot
plot.xlim(-10, 10)
plot.ylim(-10, 10)
def update(x, vitesse, temps, theta):
    x1=x[0]+vitesse*temps*np.cos(theta)
    y1=x[1]+vitesse*temps*np.sin(theta)
    return [x1, y1]

def driver(x):
    while True:
        temps = random.random()
        vitesse = random.random()
        theta = np.random.uniform(0, 2*np.pi)
        x = update(x, vitesse, temps, theta)
        if -10<x[0]<10 and -10<x[1]<10:
            print(x)
            return x
x = np.array(([0,0]))
driver(x)
# Exercice 1.3
def run():
    x = [0, 0]
    for i in range(1000):
        x=driver(x)
        plot.plot(x[0], x[1], 'b+')
        print(x)
        plot.pause(0.1)
    plot.show()

run()
