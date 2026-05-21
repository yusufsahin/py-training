#Class tanımla

class Arac:
    def __init__(self, marka,model):
        self.marka = marka
        self.model = model

class Araba(Arac):
    sayac=0
    def __init__(self, marka,model,kapi_sayisi):
        super().__init__(marka,model)
        self.kapi_sayisi = kapi_sayisi
        Araba.sayac+=1
    def __str__(self):
        return f"{self.marka} {self.model} {self.kapi_sayisi}"
    def bilgi(self):
        return f"{self.marka} {self.model}  {self.kapi_sayisi}"
    @classmethod
    def araba_sayisi(cls):
        return cls.sayac


class Motosiklet(Arac):
    def __init__(self, marka,model,selesivarmi):
        super().__init__(marka,model)
        self.selesivarmi = selesivarmi
    def __str__(self):
        return f"{self.marka} {self.model} {self.selesivarmi}"

araba1=Araba("Honda","CRV","5")
print(araba1.bilgi())
print("Araba sayisi : ",Araba.araba_sayisi())

araba2=Araba("Toyota","Corolla","4")
print(araba2.__str__())
print("Araba sayisi : ",Araba.araba_sayisi())

motosiklet1=Motosiklet("Suzuki","Hayabusa",False)
print(motosiklet1.__str__())
print("Araba sayisi : ",Araba.araba_sayisi())

araba3=Araba("Nissan","Qashqai",5)
print(araba3.bilgi())
print("Araba sayisi : ",Araba.araba_sayisi())

class Vektor:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vektor(self.x+other.x,self.y+other.y)
    def __str__(self):
        return f"{self.x} {self.y}"

vektor1=Vektor(1,2)
vektor2=Vektor(2,3)
vektor3=vektor1+vektor2

print(vektor3)

class Dikdortgen:
    def __init__(self,en,boy):
        self.en = en
        self.boy = boy
    @property
    def alan(self):
        return self.en*self.boy
    #def alan(self):
    #    return self.en*self.boy

dikdortgen1=Dikdortgen(5,3)
##print(dikdortgen1.alan())
print(dikdortgen1.alan)



