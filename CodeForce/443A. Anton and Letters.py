def anton_and_letters():
    inp = input()
    letters = [l for l in inp[1:len(inp)-1].split(', ') if l]

    letter_set = set()
    for letter in letters:
        if letter not in letter_set:
            letter_set.add(letter)
    return len(letter_set)


if __name__ == '__main__':
    print(anton_and_letters())
