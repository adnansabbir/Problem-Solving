class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s or not len(s) or s == " ":
            return 0

        length_of_string = len(s) - 1

        while length_of_string >= 0:
            if s[length_of_string] == ' ':
                length_of_string -= 1
            else:
                break

        length_of_last_word = 0
        while length_of_string >= 0:
            if s[length_of_string] == ' ':
                return length_of_last_word
            else:
                length_of_string -= 1
                length_of_last_word += 1

        return length_of_last_word


solution = Solution()
print(solution.lengthOfLastWord('Hello Worlda'))

# Time Complexity O(n) here n is the length of last word including ending space
