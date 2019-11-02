from typing import List


# Implemented Binary search as a sorted array is given as input
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        if nums[start] > target:
            return start
        elif nums[end] < target:
            return end + 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start


solution = Solution()
print(solution.searchInsert([1, 3, 3, 5, 5, 5, 6, 8, 9, 9], 7))

# Time Complexity - > O(log(n))
