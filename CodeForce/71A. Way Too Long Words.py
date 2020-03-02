def way_too_long_word():
    num_of_words = int(input())

    for i in range(num_of_words):
        word = input()
        if len(word) > 10:
            print(f'{word[0]}{len(word) - 2}{word[-1]}')
        elif word:
            print(word)


if __name__ == '__main__':
    while True:
        way_too_long_word()



