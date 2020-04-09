class Solution:
    def reverse(self, x: int) -> int:
        multiplier = 1 if x >= 0 else -1
        x *= multiplier
        reversed_x = 0
        limit = [(-2 ** 31), (2 ** 31) - 1]
        while x:
            reversed_x = reversed_x * 10 + (x % 10)
            x = x // 10

            if not limit[0] < reversed_x < limit[1]:
                return 0

        return reversed_x * multiplier


sol = Solution()
print(sol.reverse(1534236469))
print(2 ** 31 - 1)
