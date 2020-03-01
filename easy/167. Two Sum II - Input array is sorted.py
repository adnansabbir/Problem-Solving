from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            return []

        visited_nums = {
            numbers[0]: 1
        }

        for i, num in enumerate(numbers[1:]):
            left = target - num
            if left in visited_nums:
                return [visited_nums[left], i + 2]
            else:
                visited_nums[num] = i + 2

        return []


sol = Solution()
print(sol.twoSum([0, 5], 5))
