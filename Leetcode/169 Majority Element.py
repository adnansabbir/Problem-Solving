from typing import List


# O(n) and S(n)
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


# print(ord('A'))


# O(n) and S(1)
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        winner, count = nums[0], 0

        for num in nums:
            if count == 0:
                winner = num
                count += 1
            else:
                if num != winner:
                    count -= 1
                else:
                    count += 1
        return winner


sol = Solution2()
print(sol.majorityElement([2, 2, 2, 3, 3]))
