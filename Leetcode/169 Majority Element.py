from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem_count = {}
        majority_len = len(nums) // 2 + len(nums) % 2

        for num in nums:
            if num in elem_count:
                elem_count[num] += 1
            else:
                elem_count[num] = 1

            if elem_count[num] >= majority_len:
                return num


sol = Solution()
print(sol.majorityElement([2,2,2,3,3]))
# print(ord('A'))
