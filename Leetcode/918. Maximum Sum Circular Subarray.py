from typing import List


class Solution(object):
    def findMinSum(self, A: List[int]):
        running_sum = 0
        min_sum = 0
        for num in A:
            running_sum += num
            if running_sum > 0:
                running_sum = 0
            if running_sum < min_sum:
                min_sum = running_sum
        return min_sum

    def findMaxSum(self, A: List[int]):
        running_sum = 0
        max_sum = 0
        for num in A:
            running_sum += num
            if running_sum < 0:
                running_sum = 0
            if running_sum > max_sum:
                max_sum = running_sum
        return max_sum

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total_sum = sum(A)
        max_subarray = self.findMaxSum(A)
        min_subarray = self.findMinSum(A)
        max_num = max(A)

        if max_num >= 0:
            return max(max_subarray, total_sum - min_subarray)
        else:
            return max_num


sol = Solution()
array = [-10, -7, 9, -7, 6, 9, -9, -4, -8, -5]
print(sol.maxSubarraySumCircular(array))
