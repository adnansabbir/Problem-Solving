def helpful_maths():
    nums = sorted(input().split('+'), key=lambda x: int(x))
    return '+'.join(nums)


if __name__ == '__main__':
    print(helpful_maths())