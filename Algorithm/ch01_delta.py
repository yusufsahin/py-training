import math

print("İkici dereceden denklem kök bulma")
print("Denklem formatı :  ax² + bx + c = 0")
print("-"*40)


print("-"*40)

print("a değerini giriniz")
a = int(input("a = "))
print("b değerini giriniz")
b = int(input("b = "))
print("c değerini giriniz")
c = int(input("c = "))

delta = b**2-4*a*c
print("Delta = ",delta)
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Delta pozitif olduğu için iki farklı gerçek kök vardır.")
    print("x1 = ",x1)
    print("x2 = ",x2)
elif delta == 0:
    x=-b/2*a
    print("x1 = x2 = ",x)
else:
    print("Delta negatif olduğu için gerçek kök yoktur.")
    print("Bu denklemin kökleri karmaşık sayıdır.")