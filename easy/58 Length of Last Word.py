class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s or not len(s) or s == " ":
            return 0

        length_of_string = len(s)

        for i in range(length_of_string - 1, -1, -1):
            if s[i] == ' ':
                length_of_string -= 1
            else:
                break

        numbers_in_last_word = 0
        for i in range(length_of_string - 1, -1, -1):
            if s[i] == ' ':
                return numbers_in_last_word
            else:
                numbers_in_last_word += 1

        return numbers_in_last_word


solution = Solution()
print(solution.lengthOfLastWord(' HelloWorlda '))
