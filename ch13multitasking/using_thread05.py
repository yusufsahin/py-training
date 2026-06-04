import threading

counter=0

def increase():
    global counter
    for _ in range(100000):
        counter+=1

thread1 = threading.Thread(target=increase)
thread2 = threading.Thread(target=increase)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Counter:", counter)

#thread aynı anda güncelleye çalışır - Race Condition