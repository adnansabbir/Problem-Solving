from typing import List
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        non_zero_product = 1
        zero_count = 0
        for num in nums:
            if not num:
                zero_count += 1
            else:
                non_zero_product *= num

        if zero_count > 1:
            return [0] * len(nums)
        elif zero_count == 1:
            for i, num in enumerate(nums):
                nums[i] = 0 if num else non_zero_product
        else:
            for i, num in enumerate(nums):
                nums[i] = non_zero_product // num

        return nums


sol = Solution()
print(sol.productExceptSelf([1, 0, 3, 4]))
