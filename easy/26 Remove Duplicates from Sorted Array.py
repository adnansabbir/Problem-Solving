from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        j = 0
        for i, num in enumerate(nums):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j + 1

# Time Complexity -> O(n)
