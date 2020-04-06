from typing import List


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        for _ in range(k):
            temp = nums[0]
            for i in range(1, len(nums)):
                nums[i], temp = temp, nums[i]

            nums[0] = temp


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        num_to_swap = nums[:k]

        if k:
            for i, num in enumerate(nums):
                index = (i + k) % len(nums)
                num_to_swap[i % k], nums[index] = nums[index], num_to_swap[i % k]


class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        temp_nums = nums.copy()

        for i, num in enumerate(temp_nums):
            nums[(i + k) % len(nums)] = num


class Solution4:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        steps = 0
        start = 0
        while steps < len(nums):
            index = start
            temp_num = nums[start]

            while True:
                next_index = (index + k) % len(nums)
                temp_num, nums[next_index] = nums[next_index], temp_num
                index = next_index
                steps += 1

                if start == index:
                    break

            start += 1


class Solution5:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


sol = Solution5()
arr = [1, 2]
sol.rotate(arr, 3)
print(arr)
