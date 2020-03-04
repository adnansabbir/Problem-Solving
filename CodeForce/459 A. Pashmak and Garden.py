def pashmak_and_garden():
    coordinates = [int(c) for c in input().split(' ')]
    x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]

    Xd = (x1 - x2)
    Yd = (y1 - y2)

    result = []
    if Xd and not Yd:
        result = [x1, y1 + abs(Xd), x2, y2 + abs(Xd)]
    elif Yd and not Xd:
        result = [x1 + abs(Yd), y1, x2 + abs(Yd), y2]
    elif Xd != 0 and Yd != 0:
        result = [x1, y2, x2, y1]

    if Xd != 0 and Yd != 0 and abs(Xd) != abs(Yd):
        return [-1]

    return result


if __name__ == '__main__':
    print(' '.join(str(x) for x in pashmak_and_garden()))
