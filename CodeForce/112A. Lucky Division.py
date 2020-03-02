def lucky_division():
    lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

    num = int(input())
    for l_n in lucky_numbers:
        if num % l_n == 0:
            return 'YES'
    return 'NO'


if __name__ == '__main__':
    print(lucky_division())
