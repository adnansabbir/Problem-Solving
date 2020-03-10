class Solution:
    def trailingZeroes(self, n: int) -> int:
        training_zero = 0
        while n:
            training_zero += n // 5
            n = n // 5
        return training_zero

sol = Solution()
print(sol.trailingZeroes(5))
# print(ord('A'))
