class Solution:
    def countAndSay(self, n: int) -> str:
        if n < 1:
            return ''
        elif n == 1:
            return '1'

        count_and_say = '1'

        for i in range(n-1):
            temp_count_and_say = ''
            previous_char = count_and_say[0]
            char_count = 0
            for ch in count_and_say:
                if ch == previous_char:
                    char_count += 1
                else:
                    temp_count_and_say += str(char_count) + previous_char
                    previous_char = ch
                    char_count = 1

            temp_count_and_say += str(char_count) + previous_char
            count_and_say = temp_count_and_say

        return count_and_say


solution = Solution()
print(solution.countAndSay(7))
