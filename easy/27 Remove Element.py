from typing import List


class Solution:
    # 2 pointer solution
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        j = len(nums) - 1

        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        return i

# Time Complexity - O(n)
