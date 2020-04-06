from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        count = 1
        for end, num in enumerate(nums):
            if num != nums[start]:
                start += 1
                nums[start], nums[end] = nums[end], nums[start]
                count += 1

        return count


sol = Solution()
arr = [1,1,2]
print(sol.removeDuplicates(arr))
print(arr)
