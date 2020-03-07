def doreamon_and_stairs():
    n, m = [int(x) for x in input().split(' ', 1)]

    if m > n:
        return -1
    elif m == n:
        return n

    two_steps = n // 2
    single_steps = n % 2

    while (two_steps + single_steps) % m != 0:
        two_steps -= 1
        single_steps += 2

        if two_steps < 0 or single_steps > n:
            return -1

    return two_steps + single_steps


if __name__ == '__main__':
    while True:
        print(doreamon_and_stairs())
