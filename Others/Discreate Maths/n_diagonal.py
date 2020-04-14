import itertools as it


class Solution:
    def find_combination(self, n):
        for perm in it.product(range(3), repeat=10):
            print(perm)


sol = Solution()
sol.find_combination(4)
