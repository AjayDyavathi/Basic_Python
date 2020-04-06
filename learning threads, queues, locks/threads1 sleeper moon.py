import threading
import time

def sleeper(n, name):
    print('Hi Iam {}.\nIam going to sleep for 5 seconds.\n'.format(name))
    time.sleep(n)
    print('Hey, {} just got up'.format(name))

t = threading.Thread(target = sleeper, name = 'thread1', args = (5,'thread1'))

t.start()
