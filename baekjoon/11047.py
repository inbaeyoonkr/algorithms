import sys
import math


def solution(money, coins):
    number = 0
    rest_money = money
    for c in coins:
        if rest_money == 0:
            break
        else:
            if c > rest_money:
                continue
            elif c == rest_money:
                rest_money -= c
                number += 1
                break
            else:
                temp = math.floor(rest_money / c)
                number += temp
                rest_money -= (c * temp)
    return number


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split())
    coins = []
    for _ in range(n):
        coin = int(sys.stdin.readline().strip())
        coins.append(coin)
    coins.sort(reverse=True)
    print(solution(k, coins))
