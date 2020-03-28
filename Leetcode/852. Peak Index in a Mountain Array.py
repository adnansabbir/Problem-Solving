from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        start = 0
        end = len(A) - 1
        mid = (start + end) // 2
        while start <= end:
            mid = (start + end) // 2
            print(start, mid, end)
            if A[mid - 1] > A[mid]:
                end = mid - 1
            elif A[mid + 1] > A[mid]:
                start = mid + 1
            else:
                return mid

        return mid


sol = Solution()
print(sol.peakIndexInMountainArray([18, 29, 38, 59, 98, 100, 99, 98, 90]))
