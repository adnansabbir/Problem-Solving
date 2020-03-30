from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i, num in enumerate(nums):
            if num:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        # i = j = 0
        # while i < len_of_nums:
        #     if nums[i] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         j += 1
        #
        #     i += 1


sol = Solution()
arr = [1, 0, 0, 0, 3]
sol.moveZeroes(arr)
print(arr)
