# RunTime = O(n). Since we are iterating only one through out the hole string


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Edge cases
        if haystack == needle or needle == '':
            return 0
        if len(haystack) < len(needle):
            return -1

        length_of_needle = len(needle)

        # Looping through haystack till end - length of string +1 because we need to include last character
        for i in range((len(haystack) - length_of_needle) + 1):
            if haystack[i:i + length_of_needle] == needle:
                return i

        return -1


solution = Solution()
print(solution.strStr("mississippi", "pi"))
