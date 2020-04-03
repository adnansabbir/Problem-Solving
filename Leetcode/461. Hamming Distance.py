class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bit_wise_xor = x ^ y
        counter = 0
        while bit_wise_xor:
            bit_wise_xor &= bit_wise_xor - 1
            counter +=1

        return counter


sol = Solution()
print(sol.hammingDistance(1, 4))
# print([(x, y) for x, y in zip(bin(1), bin(100))])
