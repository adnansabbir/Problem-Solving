from typing import List


class Solution:
    @staticmethod
    def findFrequency(phrase: str):
        char_frequency = [0] * 26
        for char in phrase:
            char_frequency[ord(char) - ord('a')] += 1
        return char_frequency

    @staticmethod
    def compareFrequency(f1, f2):
        for i in range(len(f1)):
            if f1[i] != f2[i]:
                return False
        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p or len(s) < len(p):
            return []

        p_frequency = self.findFrequency(p)
        s_frequency = self.findFrequency(s[0:len(p)])

        p_length = len(p)
        s_length = len(s)
        anagram_indexes = []

        if self.compareFrequency(p_frequency, s_frequency):
            anagram_indexes.append(0)

        for index in range(1, (s_length - p_length + 1)):
            s_frequency[ord(s[index - 1]) - ord('a')] -= 1
            s_frequency[ord(s[index + p_length - 1]) - ord('a')] += 1

            if self.compareFrequency(p_frequency, s_frequency):
                anagram_indexes.append(index)

        return anagram_indexes


sol = Solution()
s = "abba"
p = "ab"
print(sol.findAnagrams(s, p))
