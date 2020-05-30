from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def findEuDistanceSq(point: [int]):
            return abs((point[0] * point[0]) + (point[1] * point[1]))

        sorted_points = sorted(points, key=findEuDistanceSq)
        return sorted_points[:K]
