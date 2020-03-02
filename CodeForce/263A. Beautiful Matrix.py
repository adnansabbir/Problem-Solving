def beautiful_matrix():
    global position
    for i in range(5):
        row = input().split(' ')
        for j, num in enumerate(row):
            if num == '1':
                return abs(i-2) + abs(j-2)


if __name__ == '__main__':
    print(beautiful_matrix())

