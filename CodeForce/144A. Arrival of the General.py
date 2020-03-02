def arrival_of_general():
    input()
    soldiers = [int(s) for s in input().split(' ')]
    max = [soldiers[0], 0]
    min = [soldiers[0], 0]

    for i, sol in enumerate(soldiers):
        if sol > max[0]:
            max = [sol, i]

        if sol <= min[0]:
            min = [sol, i]
    return (max[1] + (len(soldiers)-min[1]-1)) if max[1] < min[1] else (max[1] + (len(soldiers)-min[1]-2))


if __name__ == '__main__':
    print(arrival_of_general())
