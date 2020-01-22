import sys
import math

coins = (500, 100, 50, 10, 5, 1)


def greedy(money):
    coin_count = 0

    for coin in coins:
        if money == 0:
            break
        else:
            if money < coin:
                continue
            elif money == coin:
                coin_count += 1
                break
            else:
                coin_count += math.floor(money / coin)
                money -= (coin * math.floor(money / coin))
    return coin_count


if __name__ == "__main__":
    price = int(sys.stdin.readline())
    print(greedy(1000-price))
