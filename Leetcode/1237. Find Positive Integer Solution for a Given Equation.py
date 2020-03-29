from typing import List


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        _range = z + 1
        for x in range(1, _range):
            start = 1
            end = _range

            while start <= end:
                y = (start + end) // 2
                c_f_x_y_val = customfunction.f(x, y)

                if c_f_x_y_val > z:
                    end = y - 1
                elif c_f_x_y_val < z:
                    start = y + 1
                elif c_f_x_y_val == z:
                    result.append([x, y])
                    start = end + 1

        return result
