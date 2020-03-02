def calculate_total_sum():
    sample = int(input())

    total_sum = [0, 0, 0]
    for i in range(sample):
        numbers = input().split(' ')
        total_sum[0] += int(numbers[0])
        total_sum[1] += int(numbers[1])
        total_sum[2] += int(numbers[1])

    return total_sum


if __name__ == '__main__':
    total = calculate_total_sum()
    if not (total[0] or total[1] or total[2]):
        print('YES')
    else:
        print('NO')
    # print('NO' if sum(total) else 'YES')
