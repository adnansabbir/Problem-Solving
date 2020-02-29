class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            if not (s[start].isalpha() or s[start].isnumeric()):
                start += 1
            elif not (s[end].isalpha() or s[end].isnumeric()):
                end -= 1
            elif s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1

        return True


sol = Solution()
print(sol.isPalindrome('a...............0A.b a0,a'))
