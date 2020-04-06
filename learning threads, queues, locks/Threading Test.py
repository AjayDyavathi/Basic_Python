import threading
from matplotlib import pyplot as plt
import os


def plotter(x):
    plt.plot(x)
    plt.show()

def speak(s):
    os.system('say {}'.format(s))

    
a = [9,8,7,6,5,4,3,2]
b = 10

t0 = threading.Thread(target = speak, name = 'thread0', args = ('plotting graph',))
t0.start()
t = threading.Thread(target = plotter, name = 'thread', args = (a,))
t.start()




