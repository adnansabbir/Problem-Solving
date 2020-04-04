class Solution:
    def maximum69Number(self, num: int) -> int:
        num_str = str(num)

        for i in range(len(num_str)):
            if num_str[i] == '6':
                return int(num_str[0:i] + '9' + num_str[i + 1:])

        return num
