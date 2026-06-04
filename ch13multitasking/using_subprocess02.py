import subprocess
import os

def run_child_process():
    process = subprocess.Popen(['python', '-c', 'import time; print("Çocuk süreci başladı."); time.sleep(5); print("Çocuk süreci bitti.")'])
    return process

if __name__ == '__main__':
    print(f"Ana süreç başladı. Süreç ID'si: {os.getpid()}")
    process = run_child_process()
    print(f"Bu ana süreç. Çocuk süreci başlatıldı. Çocuk süreci ID'si: {process.pid}")
    process.wait()
    print("Ana süreç: Çocuk süreci tamamlandı.")