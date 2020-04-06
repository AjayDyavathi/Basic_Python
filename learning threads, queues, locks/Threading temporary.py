import threading
from matplotlib import pyplot as plt
import os
import time

def plotter(x):
    #plt.plot(x)
    #plt.show()
    #os.system('say {}'.format(x))
    #print (1243123456781234567823456783456783456784567)
    for i in range(10):
        print(i)
        time.sleep(.1)
        

def speak(s):
    os.system('say {}'.format(s))

    
a = [9,8,7,6,5,4,3,2]
b = 10

t0 = threading.Thread(target = speak, name = 'thread0', args = ('threading initiated',))

t = threading.Thread(target = plotter, name = 'thread', args = ('happening again',))
t0.start()
t.start()




