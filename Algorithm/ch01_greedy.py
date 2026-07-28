def greedy_change(amount, coins):
    result = []

    print("Başlangıç tutarı:", amount)
    print("Kullanılabilecek paralar:", coins)
    print("-" * 45)

    for coin in coins:
        print(f"Şu an kontrol edilen para: {coin}")

        while amount >= coin:
            result.append(coin)
            amount -= coin

            print(f"  {coin} seçildi")
            print(f"  Kalan tutar: {amount}")
            print(f"  Şimdiki sonuç: {result}")

        print("-" * 45)

    return result


coins = [25, 10, 5, 1]

change = greedy_change(87, coins)

print("Sonuç:", change)
print("Madeni para sayısı:", len(change))