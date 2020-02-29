from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals_traiangle = []
        for i in range(1, numRows + 2):
            sub_array = [1] * i
            pascals_traiangle.append(sub_array)

        if len(pascals_traiangle) > 2:
            for height, row in enumerate(pascals_traiangle[2:]):
                for i in range(1, len(row) - 1):
                    row[i] = pascals_traiangle[height+1][i] + pascals_traiangle[height+1][i-1]
        return pascals_traiangle


sol = Solution()
for i in sol.generate(2):
    print(i)
