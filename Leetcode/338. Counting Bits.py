from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        no_of_1s = [0] * (num + 1)

        for power in range(0, 32):
            start, end = 1 << power, 1 << (power + 1)

            if start > num:
                break

            for number in range(start, min(num + 1, end)):
                no_of_1s[number] = no_of_1s[number - start] + 1

        return no_of_1s
