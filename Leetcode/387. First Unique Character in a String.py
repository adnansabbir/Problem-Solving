class Solution:
    def firstUniqChar(self, s: str) -> int:
        ch_dict = {}
        for char in s:
            if char in ch_dict:
                ch_dict[char] += 1
            else:
                ch_dict[char] = 1

        for i, char in enumerate(s):
            if ch_dict[char] == 1:
                return i
        return -1


sol = Solution()
print(sol.firstUniqChar('loveleetcode'))
