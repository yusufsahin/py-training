import multiprocessing
import os
import time
from datetime import datetime


def log(message):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {message}", flush=True)


def child_process():
    log("CHILD  : Çocuk süreç başladı.")
    log(f"CHILD  : Child PID       = {os.getpid()}")
    log(f"CHILD  : Parent PID      = {os.getppid()}")

    for i in range(1, 6):
        log(f"CHILD  : Çalışıyor... {i}/5")
        time.sleep(1)

    log("CHILD  : Çocuk süreç bitti.")

if __name__ == "__main__":
    log("PARENT : Ana süreç başladı.")
    log(f"PARENT : Parent PID      = {os.getpid()}")

    log("PARENT : Çocuk süreç oluşturuluyor...")
    p = multiprocessing.Process(target=child_process)

    log("PARENT : Çocuk süreç başlatılıyor...")
    p.start()

    log(f"PARENT : Çocuk süreç başlatıldı. Child PID = {p.pid}")

    log("PARENT : Şimdi p.join() çağrılıyor.")
    log("PARENT : Ana süreç burada çocuk sürecin bitmesini bekleyecek.")

    p.join()

    log("PARENT : p.join() bitti.")
    log("PARENT : Çocuk süreç tamamlandı.")
    log("PARENT : Ana süreç devam ediyor ve kapanıyor.")