from typing import List


class Solution:
    @staticmethod
    def find_index_of_max_num(nums: List[int], start: int, end: int):
        mid = (start + end) // 2

        # The array is not rotated
        if nums[start] < nums[end]:
            return end

        # if there is only 1 elem
        if start == end:
            return start

        # if mid+1 is smaller than mid, it is the largest
        if mid < end and nums[mid + 1] < nums[mid]:
            return mid

        # if mid-1 is greater than mid, mid-1 is the largest
        if mid > start and nums[mid - 1] > nums[mid]:
            return mid - 1

        if nums[start] > nums[mid]:
            return Solution.find_index_of_max_num(nums, start, mid - 1)
        else:
            return Solution.find_index_of_max_num(nums, mid + 1, end)

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        pivot = self.find_index_of_max_num(nums, 0, len(nums) - 1)
        start = 0
        end = len(nums) - 1

        if nums[pivot] == target:
            return pivot

        if target >= nums[start]:
            end = pivot - 1
        else:
            start = pivot + 1

        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return -1


sol = Solution()
arr = [1, 2, 3, 4, 5, 6, 7, -3, -2, -1, 0]
print(sol.search(arr, 5))
