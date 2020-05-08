from typing import List


class Solution:
    def findSlope(self, point_a: List[int], point_b: List[int]):
        if point_a[0] == point_b[0]: return 0
        return (point_a[1] - point_b[1]) / (point_a[0] - point_b[0])

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        g_slope = self.findSlope(coordinates[0], coordinates[1])

        for i, coordinate in enumerate(coordinates[1:]):
            if g_slope != self.findSlope(coordinates[i], coordinate):
                return False

        return True


sol = Solution()
arr = [[-7, -3], [-7, -1], [-2, -2], [0, -8], [2, -2], [5, -6], [5, -5], [1, 7]]
# print(sol.checkStraightLine(arr))
