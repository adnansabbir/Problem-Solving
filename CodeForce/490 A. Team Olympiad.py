def team_olympiad():
    n = int(input())
    members = [int(x) for x in input().split(' ')]

    programming = []
    maths = []
    pe = []

    for i, member in enumerate(members):
        if member == 1:
            programming.append(i + 1)
        if member == 2:
            maths.append(i + 1)
        if member == 3:
            pe.append(i + 1)

    min_number_of_possible_teams = min(len(programming), len(maths), len(pe))
    if min_number_of_possible_teams:
        print(min_number_of_possible_teams)
        for i in range(min_number_of_possible_teams):
            print(f'{programming[i]} {maths[i]} {pe[i]}')
    else:
        print(0)


if __name__ == '__main__':
    while True:
        team_olympiad()
