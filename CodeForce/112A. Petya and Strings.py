def petya_and_strings():
    string1 = input()
    string2 = input()

    for i, char in enumerate(string1):
        d = ord(char.lower()) - ord(string2[i].lower())
        if d > 0:
            return 1
        if d < 0:
            return -1

    return 0


if __name__ == '__main__':
    print(petya_and_strings())
