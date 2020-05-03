class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j_set = set(J)
        return len([x for x in S if x in j_set])


sol = Solution()
print(sol.numJewelsInStones("aA", "aAAbbbb"))
