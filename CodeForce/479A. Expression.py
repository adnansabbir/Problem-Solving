def expression():
    nums = []
    for i in range(3):
        nums.append(int(input()))

    middle_num_max_with_left = max(nums[0] * nums[1], nums[0] + nums[1])
    middle_num_max_with_right = max(nums[2] * nums[1], nums[2] + nums[1])
    max_val = max(
        nums[0] * middle_num_max_with_right,
        nums[0] + middle_num_max_with_right,
        nums[2] + middle_num_max_with_left,
        nums[2] * middle_num_max_with_left,
    )

    return max_val


if __name__ == '__main__':
    print(expression())
