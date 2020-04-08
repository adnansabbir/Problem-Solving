from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        length_of_str = len(s)
        for i in range(length_of_str // 2):
            s[i], s[length_of_str - i - 1] = s[length_of_str - i - 1], s[i]


sol = Solution()
arr = list('hellop')
sol.reverseString(arr)
print(arr)
