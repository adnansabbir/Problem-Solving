from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        num_dict = set(arr)

        ce = 0
        for num in arr:
            if num + 1 in num_dict:
                ce += 1

        return ce


sol = Solution()
print(sol.countElements([1, 1, 2, 2]))
