#Paralar: [1, 3, 4]
#Tutar: 6

def minimum_coins(amount, coins):
    infinity = float("inf")

    dp = [infinity] * (amount + 1)
    selected_coin = [None] * (amount + 1)

    dp[0] = 0

    for current_amount in range(1, amount + 1):
        print(f"\nHesaplanan tutar: {current_amount}")

        for coin in coins:
            if coin <= current_amount:
                previous_amount = current_amount - coin

                candidate = dp[previous_amount] + 1

                print(
                    f"  {coin} kullanılırsa: "
                    f"dp[{previous_amount}] + 1 = {candidate}"
                )

                if candidate < dp[current_amount]:
                    dp[current_amount] = candidate
                    selected_coin[current_amount] = coin

                    print(
                        f"  Yeni en iyi sonuç: "
                        f"dp[{current_amount}] = {candidate}"
                    )

        print("DP tablosu:", dp)

    if dp[amount] == infinity:
        return None

    result = []
    remaining = amount

    while remaining > 0:
        coin = selected_coin[remaining]
        result.append(coin)
        remaining -= coin

    return result


result = minimum_coins(
    amount=6,
    coins=[1, 3, 4]
)

print("\nSeçilen paralar:", result)
print("Minimum para sayısı:", len(result))