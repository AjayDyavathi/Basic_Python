import threading
import queue
import numpy as np
import time


event  = threading.Event()

def flag():
    print('Starting program in 3 sec...')
    time.sleep(3)
    event.set()
    print('Starting countdown..\n')
    time.sleep(7)
    event.clear()
    print('event is cleared..!\n')

def start_operation():
    event.wait()
    while event.is_set():
        print('Starting task of random integers..')
        x = np.random.randint(1,30)
        time.sleep(.5)
        if x == 29:
            print('True')
    print('Event has been cleared, so random task stops..')

t1 = threading.Thread(target = flag)
t2 = threading.Thread(target = start_operation)

t1.start()
t2.start()
