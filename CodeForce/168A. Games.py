def games():
    num_of_teams = int(input())

    hj = []
    gj = {}
    for i in range(num_of_teams):
        jersey = [int(j) for j in input().split(' ')]
        hj.append(jersey[0])

        if jersey[1] in gj:
            gj[jersey[1]] += 1
        else:
            gj[jersey[1]] = 1

    total = 0
    for color in hj:
        if color in gj:
            total += gj[color]

    return total


if __name__ == '__main__':
    print(games())
