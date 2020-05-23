from typing import List


class Solution:
    @staticmethod
    def findIntersection(A: List[int], B: List[int]):
        intrs = [max(A[0], B[0]), min(A[1], B[1])]
        return intrs if intrs[0] <= intrs[1] else []

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        intersections = []

        for intervalA in A:
            for intervalB in B:

                if intervalA[1] < intervalB[0]:
                    break
                if intervalA[0] > intervalB[1]:
                    continue

                intersection = self.findIntersection(intervalA, intervalB)
                if intersection:
                    intersections.append(intersection)

        return intersections
