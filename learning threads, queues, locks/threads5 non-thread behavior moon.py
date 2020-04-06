#this is comparision between threas and non-threads

import time


def sleeper(n, name):
    print("Hi! Iam thread {}, going to sleep for 5 sec.\n".format(name))
    time.sleep(n)
    print("{} just got up\n\n".format(name))

start = time.time()

for i in range(5):
    print("iteration",i,"has started")
    sleeper(5,i)

end = time.time()

print("time taken:",end-start)
