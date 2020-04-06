import threading
import time

class MyThread(threading.Thread):
    def __init__(self, number, func, args):
        threading.Thread.__init__(self)
        self.number = number
        self.func = func
        self.args = args

    def run(self):
        print('Thread {} has started'.format(self.number))
        self.func(*self.args)
        print('Thread {} has finished'.format(self.number))

def double(number,cycles):
     for i in range (cycles):
         number+=number
     print(number)

threads_list = []

for i in range(7):
    t = MyThread(number = i+1, func = double, args = [i,10])
    threads_list.append(t)
    t.start()
    #t.join()
    
for t in threads_list:
    t.join()

