with open('example.txt','r') as f:
    f.seek(10) #10.byte'a git
    data=f.read(5) #sonraki 5. byte'ı oku
    print(data)

    position=f.tell()
    print(position)