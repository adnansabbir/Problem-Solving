class Solution:
    def convertToTitle(self, n: int) -> str:
        alpha_num = ""

        while n:
            modVal = n % 26
            if modVal:
                alpha_num += chr(64 + modVal)

            elif modVal == 0:
                alpha_num += "Z"

            n = (n // 26)
            if modVal == 0:
                n -=1

        return alpha_num[::-1]


sol = Solution()
print(sol.convertToTitle(701))
# print(ord('A'))
