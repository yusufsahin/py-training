import pickle

data={'isim':'Alice','yas':25}

with open("data.pickle","wb") as file:
    pickle.dump(data,file,protocol=pickle.HIGHEST_PROTOCOL)

with open("data.pickle","rb") as file:
    data = pickle.load(file)
    print(data)