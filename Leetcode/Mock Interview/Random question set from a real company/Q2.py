class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bit_wise_xor = x ^ y
        return bin(bit_wise_xor).count('1')


sol = Solution()
print(sol.hammingDistance(1, 5))
