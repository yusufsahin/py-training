import os
from pathlib import Path

current_dir=os.path.dirname(__file__)
file_path=os.path.join(current_dir,'example.txt')

#Dosya yazma modunda açma

with open(file_path,'w') as file:
    file.write("Hello World!\n")
    file.write("Hello World!\n")
    file.write("Hello World!\n")
    file.write("Bu, os modülü ile belirtilen dosya yoludur")

#pathlib kullanarak dosya yolu oluşturma

current_dir=Path(__file__).parent
file_path=current_dir/'ogrenci.csv'
with open(file_path,'w') as file:
    file.write("1;John;Doe;Physics\n")
    file.write("2;Sam;Doe;Math\n")
    file.write("3;Sam;Doe;Chemistry\n")
    file.write("Bu, pathlib modülü ile belirtilen dosya yoludur.\n")