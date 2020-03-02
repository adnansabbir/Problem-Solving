def string_task():
    string = input()

    vowels = {'A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y'}
    new_string = ''
    for char in string:
        if char not in vowels:
            new_string += '.' + char.lower()

    print(new_string)


if __name__ == '__main__':
    string_task()
