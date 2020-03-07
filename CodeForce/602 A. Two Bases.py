def num_with_base_to_int(num_arr, base):
    num = 0
    for i, digit in enumerate(num_arr):
        num = num*base + int(digit)
    return num


def two_base():
    _, baseX = [int(x) for x in input().split(' ')]
    numX = input().split(' ')

    _, baseY = [int(x) for x in input().split(' ')]
    numY = input().split(' ')

    XToInt = num_with_base_to_int(numX, baseX)
    YToInt = num_with_base_to_int(numY, baseY)

    # print(XToInt, YToInt)

    if XToInt < YToInt:
        return '<'
    elif XToInt > YToInt:
        return '>'
    elif XToInt == YToInt:
        return '='


if __name__ == "__main__":
    while True:
        print(two_base())
