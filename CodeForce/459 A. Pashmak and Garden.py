def pashmak_and_garden():
    coordinates = [int(c) for c in input().split(' ')]
    y1, x1, x2, y2 = coordinates[1], coordinates[0], coordinates[2], coordinates[3]

    Xd = abs(x1 - x2)
    Yd = abs(y1 - y2)

    if Xd and not Yd:
        return [x1, y1 + Xd, x2, y2 + Xd]
    elif Yd and not Xd:
        return [x1 + Yd, y1, x2 + Yd, y2]
    elif Xd == Yd and Xd != 0:
        return [x1, y2, x2, y1]
    else:
        return [-1]


if __name__ == '__main__':
    print(' '.join(str(x) for x in pashmak_and_garden()))
