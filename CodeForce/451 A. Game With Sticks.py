def game_with_stick():
    row_col = input().split(' ')

    even = min(int(row_col[0]), int(row_col[1])) % 2 == 0
    return 'Malvika' if even else 'Akshat'


if __name__ == '__main__':
    while True:
        print(game_with_stick())