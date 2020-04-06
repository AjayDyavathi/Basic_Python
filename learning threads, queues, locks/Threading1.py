import threading
import time

total = 7

def creates_items():
    global total;
    for i in  range(10):
        time.sleep(2)
        total+=1
        print('added item')

    print('Creation 1 is done!')

def creates_items_2():
    global total
    for i in range(7):
        time.sleep(2)
        total+=1
        print('Added item')

    print('Creation2 is done..')

def limits():
    global total
    while True:
        if total > 5:
            print('overload')
            total-=3
            print('Subtracted from total')

        else:
            time.sleep(2)
            print('waiting..')

creator1 = threading.Thread(target = creates_items)
creator2 = threading.Thread(target = creates_items_2)
limittor = threading.Thread(target = limits, daemon = True)

print(limittor.isDaemon())

creator1.start()
creator2.start()
limittor.start()


creator1.join()
creator2.join()
#limittor.join()


print('The final value of total is', total)
            
    
    
    
