from typing import List


class Solution:
    @staticmethod
    def isSelfDivisible(num):
        num_str = str(num)
        for digit in num_str:
            if digit == '0' or num % int(digit) != 0:
                return False
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [num for num in range(left, right+1) if self.isSelfDivisible(num)]


sol = Solution()
print(sol.selfDividingNumbers(1,1000))
