#Amaç KDV li fiyat

prices=[27,35,49,33,70,29]
print(prices)
with_tax=[]
print(with_tax)

for price in prices:
    with_tax.append(price*1.20)
print(with_tax)