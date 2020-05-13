class Solution:
    def removeDigit(self, num: str, k: int) -> str:
        numbers_left_to_delete = k
        start = 1
        length_of_str = len(num)

        while start < length_of_str and numbers_left_to_delete:
            # print(start, length_of_str, num)
            if int(num[start]) < int(num[start - 1]):
                num = num[:start - 1] + num[start:]
                length_of_str -= 1
                start -= 1
                numbers_left_to_delete -= 1
            else:
                start += 1

            if not start:
                start = 1
        return num[:-numbers_left_to_delete] if numbers_left_to_delete else num

    def removeKdigits(self, num: str, k: int) -> str:
        num = self.removeDigit(num, k).lstrip('0')
        return num or '0'


sol = Solution()
print(sol.removeKdigits('678234', 3))
# print("123"[:-0])
