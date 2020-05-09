from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target_array = []
        for n, i in zip(nums, index):
            target_array.insert(i, n)
        return target_array


sol = Solution()
print(sol.createTargetArray([1,2,3,4,0], [0,1,2,3,0]))
