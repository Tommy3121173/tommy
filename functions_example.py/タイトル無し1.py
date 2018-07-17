# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 17:26:14 2018

@author: tommy_mizuki
"""

#import matplotlib.animation as animation
#from IPython.display import HTML
#import matplotlib.pyplot as plt
#import numpy as np
## 1. Create a figure window. 
#fig = plt.figure()
## 2. Creates axes within the window
#ax = plt.axes(xlim=(0,1), ylim=(-1,1))
#
#
#e = np.e
#T1 = 1
#T2 = 1/3
#def rx(t):
#    return e**(-t/T1)
#def ry(t) :
#    return 2*np.cos(t/T2)
#
#
#def animate(t):
#    t /= 10
#    if t == 0:
#        s = t
#    else:
#        s = np.linspace(0, t)
#    x = e**(-s/T1)
#    y = 2*np.cos(s/T2)
#    ax.plot(x,y, 'c')
#
#ani = animation.FuncAnimation(fig, animate,frames=30, interval=50)
#ani
from matplotlib import animation, rc
from IPython.display import HTML
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
#import time



# Creates a figure window.
fig = plt.figure()

# Creates axes within the window
ax = plt.axes(xlim=(0, 1), ylim=(-2,2))

# Object to animate
point, = ax.plot([1], [1], marker='o', ms=40)  # for points

e =np.e
T1 = 1
T2 = 1/3

# Position of mass as function of time
def fun(s):
    x = e**(-s/T1)
    y =2*np.cos(s/T2)
    return x, y

def animate(i):   
    x, y = fun(i/10)   
    point.set_data(x, y)    
    return  (point,)
    
# Animates the data
# 50 frames
# 50ms delay between frames : animation plays at double speed of time-varying system
anim = animation.FuncAnimation(fig, animate, frames=30, interval=50, blit=True)

anim

