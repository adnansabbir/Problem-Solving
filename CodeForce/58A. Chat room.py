def chat_room():
    string = input()
    if len(string)<5:
        return 'NO'

    hello = ['o', 'l', 'l', 'e', 'h']
    for char in string:
        if not hello:
            return 'YES'
        if char == hello[-1]:
            hello.pop()

    return 'YES' if len(hello) == 0 else 'NO'


if __name__ == '__main__':
    while True:
        print(chat_room())
