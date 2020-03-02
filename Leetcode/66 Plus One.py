from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return digits

        digits.insert(0, 0)
        last_index = len(digits) - 1
        while last_index >= 0:
            if digits[last_index] == 9:
                digits[last_index] = 0
                last_index -= 1
            else:
                digits[last_index] += 1
                break
        if digits[0] == 0:
            digits.pop(0)
        return digits


solution = Solution()
print(solution.plusOne([1,2,3]))
