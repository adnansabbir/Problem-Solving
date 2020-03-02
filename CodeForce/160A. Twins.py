def twins():
    if not int(input()):
        return 0

    coins = sorted(input().split(' '), key=lambda x: int(x))
    total_money = sum([int(coin) for coin in coins])

    min_coins = 0
    partial_sum = 0
    for coin in coins[::-1]:
        partial_sum += int(coin)
        min_coins += 1
        if partial_sum > total_money//2:
            return min_coins


if __name__ == '__main__':
    print(twins())
