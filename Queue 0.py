import queue

q = queue.Queue()                   #First IN First OUT

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(),'    ')

print('\n\n\n')

import queue

q = queue.LifoQueue()               #Last IN First OUT

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())
    

print('\n\n\n')

import queue

q = queue.PriorityQueue()           #Irregular IN Lowest OUT First


q.put(5)
q.put(7)
q.put(2)
q.put(4)
q.put(3)

for i in range(q.qsize()):
    print(q.get())


print('\n\n\n')

import queue

q = queue.PriorityQueue()

q.put((5, 'Priority 5'))
q.put((7, 'Priority 7'))
q.put((4, 'Priority 4'))
q.put((2, 'Priority 2'))
q.put((3, 'Priority 3'))

for i in range(q.qsize()):
    print(q.get()[1])
