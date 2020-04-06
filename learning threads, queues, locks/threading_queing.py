import threading
from queue import Queue
import time

q = Queue()

print_lock = threading.Lock()


def exampleJob(worker):
    time.sleep(0.5)

    with print_lock:
        print(threading.current_thread().name, worker)
                                                                    
def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()


for x in range(10):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()
    

start = time.time()

for worker in range(20):
    q.put(worker)

q.join()

end = time.time()

print("Total time taken is: ",end-start)


    
