from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for num in nums[1:]:
            res = res ^ num

        return res


sol = Solution()
print(sol.singleNumber([7, 1, 2, 1, 2]))

# print(3 ^ 4)
