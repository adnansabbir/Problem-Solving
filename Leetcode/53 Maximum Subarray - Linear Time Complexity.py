from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_value = nums[0]
        current_max = nums[0]
        for num in nums[1:]:
            if current_max < 0:
                current_max = num
            else:
                current_max += num

            if current_max > max_value:
                max_value = current_max
        return max_value


# O(n) time O(1)Space
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        for i, num in enumerate(nums[1:]):
            if num + nums[i] > num:
                nums[i+1] = num + nums[i]
            if nums[i+1] > max_sum:
                max_sum = nums[i+1]
        return max_sum


solution = Solution2()
print(solution.maxSubArray([-100, 1, 2, 3, 4, 5, 6, -50, 5, 5, 5, 5, 5, 5]))
