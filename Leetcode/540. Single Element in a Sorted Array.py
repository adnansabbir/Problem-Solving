from typing import List


# O(N)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]

        return nums[-1]


# O(logn)
class Solution2:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)
        mid = 0
        while start <= end:
            mid = (start + end) // 2

            if mid + 1 < len(nums) and nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]

            if mid % 2 == 0:
                if mid + 1 < end and nums[mid] != nums[mid + 1]:
                    end = mid - 1
                else:
                    start = mid + 2
            else:
                if mid + 1 < end and nums[mid] != nums[mid + 1]:
                    start = mid + 1
                else:
                    end = mid - 1
        return nums[mid]


sol = Solution2()
print(sol.singleNonDuplicate([1, 2, 2]))
