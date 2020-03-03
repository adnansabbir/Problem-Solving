def dubstep():
    words = input().split('WUB')

    return ' '.join([word for word in words if word])


if __name__ == '__main__':
    print(dubstep())
