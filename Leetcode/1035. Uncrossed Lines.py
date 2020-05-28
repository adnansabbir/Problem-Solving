from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        A = [0] + A
        B = [0] + B

        h, w = len(A), len(B)
        dp = [[0 for x in range(w)] for y in range(h)]

        for x in range(1, h):
            for y in range(1, w):

                if A[x] == B[y]:
                    dp[x][y] = dp[x - 1][y - 1] + 1
                else:
                    dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])

        return dp[-1][-1]
