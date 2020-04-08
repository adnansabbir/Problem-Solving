import sys

while True:
    try:
        input_list = [int(x) for x in input().split()[1:]]
        n = len(input_list) - 1
        sum_of_jj = (n * (n + 1)) / 2

        difference_set = set()
        for i, num in enumerate(input_list[1:]):
            abs_val = abs(input_list[i] - num)
            # print(abs_val)
            if 0 < abs_val <= n:
                difference_set.add(abs_val)

        # print(difference_set, sum_of_jj)
        if sum(difference_set) == sum_of_jj and len(difference_set) == n:
            print("Jolly")
        else:
            print("Not jolly")

    except EOFError:
        break

print("Broken")
