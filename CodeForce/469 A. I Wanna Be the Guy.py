def wanna_be_the_guy():
    levels = list(range(1, int(input()) + 1))

    X = [int(num) for num in input()[2:].split(' ') if num]
    Y = [int(num) for num in input()[2:].split(' ') if num]

    for num in X:
        levels[num - 1] = 0

    for num in Y:
        levels[num - 1] = 0

    return 'Oh, my keyboard!' if sum(levels) else 'I become the guy.'


if __name__ == '__main__':
    print(wanna_be_the_guy())
