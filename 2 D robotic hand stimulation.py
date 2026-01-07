import math

from matplotlib import pyplot as plt
from matplotlib.pyplot import plot

#arms length
l1=5
l2=3

#angle
theta1=float(input("enter the angle 1:"))
theta2=float(input("enter the angle 2:"))

# angle in radians
t1=math.radians(theta1)
t2=math.radians(theta2)

# base point
x0,y0=0,0

#joint points
x1=l1*math.cos(t1)
y1=l1*math.sin(t1)

# end points
x2=x1+l2*math.cos(t1+t2)
y2=y1+l2*math.sin(t1+t2)

# plot
plt.plot([x0, x1, x2], [y0, y0, y2], marker='o')
plt.title('Stimulation with robotic hand')
plt.axis('equal')
plt.grid(True)
plt.show()
