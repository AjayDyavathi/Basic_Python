import threading
import time

total = 4

def create_items_1():
    global total
    for i in range(10):
        time.sleep(1)
        print("added 1 item")
        total+=1
    print("Creation is done!")

def create_items_2():
    global total
    for i in range(7):
        time.sleep(2)
        print("added 1 item")
        total+=1
    print("Creation is done!!")


def limit():
    global total
    
    while True:
        if total>5:
            print("overload")
            total = total-3
            print("Subtracted 3")
        else:
            time.sleep(1)
            print("waiting...!")


creator1 = threading.Thread(target = create_items_1)
creator2 = threading.Thread(target = create_items_2)
limitor = threading.Thread(target = limit,daemon = True)

print(limitor.isDaemon())



creator1.start()
creator2.start()
limitor.start()

creator1.join()
creator2.join()
#limitor.join()


print("the ending value is ", total)
        
    
