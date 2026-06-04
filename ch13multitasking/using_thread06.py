import threading

counter = 0
lock = threading.Lock()


def increase():
    global counter

    for _ in range(100000):
        with lock: #Race condition olmaz
            counter += 1 #Aynı anda 1 thread güncelleme yapar


thread1 = threading.Thread(target=increase)
thread2 = threading.Thread(target=increase)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Counter:", counter)