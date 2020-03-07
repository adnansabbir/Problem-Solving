def dragon():
    s, n = [int(x) for x in input().split(' ', 1)]

    dragons = []
    for i in range(n):
        dragons.append([int(x) for x in input().split(' ')])

    dragons = sorted(dragons, key=lambda x: x[0])

    for d in dragons:
        if s <= d[0]:
            return 'NO'
        else:
            s += d[1]

    return 'YES'


if __name__ == '__main__':
    while True:
        print(dragon())
