class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


sol = Solution()
for i in range(1, 21):
    print(i, sol.canWinNim(i))