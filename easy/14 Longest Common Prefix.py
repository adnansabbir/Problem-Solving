from typing import List


class Solution:
    # Used Recursion
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # EdgeCase
        if not strs or not len(strs):
            return ""

        if len(strs) == 1:
            return strs[0]

        # If more then 2 element in array divide it into 2
        if len(strs) > 2:
            str1 = self.longestCommonPrefix(strs[:len(strs) // 2])
            str2 = self.longestCommonPrefix(strs[len(strs) // 2:])
        else:
            str1 = strs[0]
            str2 = strs[1]

        lcp = ""
        for i, ch in enumerate(str1):
            if i < len(str2) and ch == str2[i]:
                lcp += ch
            else:
                return lcp
        return lcp


solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))

# TimeComplexity -> O(S)/ Since we are iterating through all the characters of each string
# Here S = m*n. m = length of each string, n = number of string
# Space Complexity - O(m.log(n)). Every time we are dividing the array into 2 and storing them
# Each stores requires M space
