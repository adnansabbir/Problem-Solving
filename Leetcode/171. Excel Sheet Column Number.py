class Solution:
    def titleToNumber(self, s: str) -> int:
        char_in_int = 0

        for i, char in enumerate(s):
            char_in_int = char_in_int*26 + (ord(char) - 64)

        return int(char_in_int)


sol = Solution()
print(sol.titleToNumber('ABC'))
# print(ord('A'))
