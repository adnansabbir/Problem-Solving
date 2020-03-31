from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_list = sum(nums)
        sum_n = (n * (n + 1)) // 2
        return sum_n - sum_of_list


sol = Solution()
print(sol.missingNumber([3, 2, 0]))