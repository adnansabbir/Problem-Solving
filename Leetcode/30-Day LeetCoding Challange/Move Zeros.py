from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = j = 0

        while j< len(nums) and nums[j]:
            j += 1
            i += 1

        while i < len(nums):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1


sol = Solution()
arr = [1, 0, 0, 0, 0]
sol.moveZeroes(arr)
print(arr)
