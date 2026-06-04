import multiprocessing
import os
import time

def worker_process(name):
    print(f'Süreç {name} (ID: {os.getpid()}) başladı')
    time.sleep(2)
    print(f'Süreç {name} (ID: {os.getpid()}) bitti')

if __name__ == '__main__':
    print(f'Ana süreç (ID: {os.getpid()}) başladı')
    process=[]
    for i in range(5):
        p = multiprocessing.Process(target=worker_process, args=(f'P{i}',))
        process.append(p)
        p.start()
    for p in process:
        p.join()
    print('Ana süreç bitti')
