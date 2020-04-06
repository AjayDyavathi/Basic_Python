import threading
import time

class MyClass(threading.Thread):
    def run(self):
        print('{} has started!!\n'.format(self.getName()))
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)

        finally:
            del self._target, self._args, self._kwargs

        print('{} has completed\n'.format(self.getName()))

def sleeper(n, name):
    print('Hi Iam {}, Going to sleep for {} seconds\n'.format(name, n))
    time.sleep(n)
    print('{} has got up!!\n'.format(name))

##t = MyClass(target = sleeper, name = 'Thread1', args = (5,'Thread1'))
##t.start()



threads_list = []

for i in range(5):
    t = MyClass(target = sleeper, name = 'Thread {}'.format(i+1), args = (5, 'Thread {}'.format(i+1)))
    t.start()
    threads_list.append(t)

for t in threads_list:
    t.join()

print('\n\nAll threads are done!!!')
    
        
                
