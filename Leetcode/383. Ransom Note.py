from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict_char = Counter(magazine)
        for ch in ransomNote:
            if ch not in magazine_dict_char or not magazine_dict_char[ch]:
                return False
            else:
                magazine_dict_char[ch] -= 1

        return True


sol = Solution()
print(sol.canConstruct("aaa", "aab"))
