import threading
import time

def sleeper(n, name):
    print("Hi!!, I'm {}. Going to sleep for 5 seconds\n".format(name))
    time.sleep(n)
    print("{} got up\n".format(name))


##t = threading.Thread(target = sleeper, name = "thread1", args = (5, 'thread1'))
##
##t.start()

threads_list = []

start = time.time()

for i in range(5):
    t = threading.Thread(target = sleeper, name = 'thread {}'.format(i), args = (5, 'thread {}'.format(i)))
    threads_list.append(t)
    t.start()
    print('thread {} has started'.format(i))

for t in threads_list:
    t.join()

end = time.time()

print('time taken:', end-start)
print('All threads are done!!')
