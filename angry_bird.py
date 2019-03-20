import math
import numpy as np
import matplotlib.pyplot as plt
Sx = 100*np.random.random()
Sy = 50*np.random.random()
plt.plot(Sx,Sy,'o')
plt.show()
V = float(input('Velocity'))
A = float(input('Angel'))



Apray = math.radians(A)
g = 9.8
x=np.arange(0,100)
y=x*math.sin(2*Apray)/2/(math.cos(Apray))**2-1/2*g*x**2/(V*math.cos(Apray))**2
pig_size = 3
distance = (x-Sx)**2+(y-Sy)**2
distance = pow(distance, 0.5)
ds=distance[distance<pig_size]
if np.shape(ds)[0] > 0:
    print("Hit!")
else:
    print("Missed!")

plt.plot(x,y)
plt.plot(Sx,Sy,'o')
plt.axis([0,100,0,50])
plt.show()

