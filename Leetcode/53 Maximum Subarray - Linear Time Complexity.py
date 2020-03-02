from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_value = max(nums)
        current_max = 0
        for num in nums:
            current_max += num
            if current_max < 0 and max_value < 0:
                current_max = max_value
            elif current_max < 0:
                current_max = 0
            max_value = max(current_max, max_value)
        return max_value


solution = Solution()
print(solution.maxSubArray([-100, 1, 2, 3, 4, 5, 6, -50, 5, 5, 5, 5, 5, 5]))
