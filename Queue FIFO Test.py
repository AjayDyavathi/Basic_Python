import threading
import time
import queue



def putting_thread(q):
    while True:
        print('Starting thread!\n')
        time.sleep(10)
        q.put(5)
        print('put something')

q = queue.Queue()

t = threading.Thread(target = putting_thread, args = (q,), daemon = True)
t.start()

q.put(7)

print(q.get())
print('first item gotten')

print(q.get())
print('finished!!')
