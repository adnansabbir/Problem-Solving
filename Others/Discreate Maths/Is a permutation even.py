# You need to write a function is_even(p) that returns True for even permutations and False for odd permutations.
# (Note that the name of the function is important. Keep the first line of the function definition unchanged!)

def is_even(p):
    counter = 0
    total_transposition = 0
    while counter < len(p):
        if counter != p[counter]:
            next_pos = p[counter]
            p[counter], p[next_pos] = p[next_pos], p[counter]
            total_transposition += 1
        else:
            counter += 1

    return total_transposition % 2 == 0


# arr = [9, 2, 12, 0, 8, 5, 7, 11, 6, 4, 10, 1, 3]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
print(is_even(arr))
