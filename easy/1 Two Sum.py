from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we are taking an object and storing the number that are already checked.
        # We are using object to search checked numbers in O(1) time
        iterated_values = {}
        for i, num in enumerate(nums):
            check_num = target - num
            if check_num in iterated_values:
                return [iterated_values[check_num], i]
            else:
                iterated_values[num] = i


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
# RunTime -> O(n) as we are iterating through the nums array and
# doing operation of checking iterated_values or storing values in O(1)
