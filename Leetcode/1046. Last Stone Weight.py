from typing import List
import bisect


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            l1 = stones.pop()
            l2 = stones.pop()

            if l1 - l2:
                bisect.insort_left(stones, abs(l1 - l2))

        stones.append(0)
        return stones[0]


arr = [2, 7, 4, 1, 8, 1]
sol = Solution()
print(sol.lastStoneWeight(arr))
