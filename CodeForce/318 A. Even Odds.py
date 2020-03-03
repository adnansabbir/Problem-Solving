def even_odds():
    inp = input().split(' ')
    total_nums, num_to_find = int(inp[0]), int(inp[1])

    mid = (total_nums + 1) // 2
    if num_to_find > mid:
        return (num_to_find - mid) * 2
    else:
        return (num_to_find * 2) - 1


if __name__ == '__main__':
    print(even_odds())
