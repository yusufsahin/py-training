import threading
import time

def download_file(file_name,duration):
    print(f"{file_name} indirilmeye başladı...")
    time.sleep(duration)
    print(f"{file_name} indirildi.")

thread1=threading.Thread(target=download_file,args=("video.mp4", 3))
thread2 = threading.Thread(target=download_file, args=("image.png", 2))
thread3 = threading.Thread(target=download_file, args=("document.pdf", 1))

#start ile başlatıyorum
thread1.start()
thread2.start()
thread3.start()
#join ile bitmesini bekliyorum
thread1.join()
thread2.join()
thread3.join()

print("Tüm dosyalar indirildi...")