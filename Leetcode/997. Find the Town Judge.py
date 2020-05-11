from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusted_arr = [0] * (N + 1)

        judge = 0
        for t in trust:
            trusted_arr[t[1]] += 1
            trusted_arr[t[0]] -= 1

        for i, t in enumerate(trusted_arr):

            if t == N - 1:
                judge = i

        return judge or -1


sol = Solution()
print(sol.findJudge(3, [[1, 3], [2, 3], [3, 1]]))
