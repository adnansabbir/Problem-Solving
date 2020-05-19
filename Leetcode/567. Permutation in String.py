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

    def checkInclusion(self, p: str, s: str) -> bool:
        if not s or not p or len(s) < len(p):
            return []

        p_frequency = self.findFrequency(p)
        s_frequency = self.findFrequency(s[0:len(p)])

        p_length = len(p)
        s_length = len(s)

        if self.compareFrequency(p_frequency, s_frequency):
            return True

        for index in range(1, (s_length - p_length + 1)):
            s_frequency[ord(s[index - 1]) - ord('a')] -= 1
            s_frequency[ord(s[index + p_length - 1]) - ord('a')] += 1

            if self.compareFrequency(p_frequency, s_frequency):
                return True

        return False


sol = Solution()
s1 = "a"
s2 = "ab"
print(sol.checkInclusion(s1, s2))
