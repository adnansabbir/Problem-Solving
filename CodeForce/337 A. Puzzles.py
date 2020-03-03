def select_puzzles():
    args = [int(a) for a in input().split(' ')]
    no_of_puzzles, total_puzzles = args[0] - 1, args[1]
    puzzles = [int(p) for p in input().split(' ')]
    puzzles.sort()

    min_diff = 1001
    for i in range(no_of_puzzles, total_puzzles):
        min_diff = min(min_diff, puzzles[i] - puzzles[i - no_of_puzzles])

    return min_diff


if __name__ == '__main__':
    print(select_puzzles())
