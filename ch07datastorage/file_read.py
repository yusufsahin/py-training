with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

with open('example.txt', 'r') as file:
    line=file.readline()
    while line:
        print(line,end='')
        line=file.readline()

with open('ogrenci.csv','r') as file:
    lines= file.readlines()
    for line in lines:
        print(line,end='')

#'for' döngüsü kullanarak dosyayı okuma
with open('ogrenci.csv','r') as file:
    for line in file:
        print(line,end='')