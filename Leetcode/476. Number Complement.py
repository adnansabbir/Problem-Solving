class Solution:
    def findComplement(self, num: int) -> int:
        num_bin_arr = ['0' if str(x) == '1' else '1' for x in bin(num)[2:]]
        return int(''.join(num_bin_arr), 2)


class Solution2:
    def findComplement(self, num: int) -> int:
        return ((1 << num.bit_length()) - 1) ^ num


sol = Solution()
print(sol.findComplement(5))
