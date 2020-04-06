import threading
import time

def sleeper(n, name):
    print("Hi! Iam thread {}, going to sleep for 5 sec.\n".format(name))
    time.sleep(n)
    print("{} just got up".format(name))

threads_list = []

start = time.time()

for i in range(5):
    t = threading.Thread(target = sleeper, name = "thread{}".format(i),
                         args = (5, "thread{}".format(i)))
    t.start()
    print("thread {} has started".format(i))
    threads_list.append(t)

for t in threads_list:
    t.join()

end = time.time()

print("time taken : ",end-start)
print("All five tasks has finished their work")
