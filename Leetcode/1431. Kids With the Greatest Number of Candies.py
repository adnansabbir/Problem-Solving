from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        can_have_max = [(candy + extraCandies) >= max_candies for candy in candies]

        return can_have_max


sol = Solution()
print(sol.kidsWithCandies([12, 1, 12], 10))
