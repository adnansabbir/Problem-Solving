from operator import mul
from functools import reduce
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_sub = {i: 0 for i in t}
        hash_t = collections.Counter(list(t))

        product_of_hash_sub_val = 0
        product_of_hash_t_val = reduce(mul, hash_t.values(), 1)
        min_sub = ''

        start = 0
        end = -1
        # product_of_hash_sub_val = reduce(mul, hash_sub.values(), 1)
        while end < len(s) - 1:
            while end < len(s) - 1 and not self.compareDict(hash_sub, hash_t):
                end += 1
                if s[end] in hash_sub:
                    hash_sub[s[end]] += 1

                product_of_hash_sub_val = reduce(mul, hash_sub.values(), 1)

            # print('After End Traversal ', s[start: end + 1], hash_sub, hash_t)
            while self.compareDict(hash_sub, hash_t):
                if (len(min_sub) > len(s[start: end + 1]) or not min_sub) and product_of_hash_sub_val:
                    min_sub = s[start: end + 1]
                    if len(min_sub) == len(t):
                        return min_sub

                if s[start] in hash_sub:
                    hash_sub[s[start]] -= 1

            #     product_of_hash_sub_val = reduce(mul, hash_sub.values(), 1)
                start += 1
            # print('After Start Traversal ', s[start: end + 1], hash_sub, hash_t)
        return min_sub

    @staticmethod
    def compareDict(phrase_dict, sub_str_dict):
        for key in phrase_dict:
            if key not in sub_str_dict or phrase_dict[key] < sub_str_dict[key]:
                return False
        return True


sol = Solution()
print(sol.minWindow('ADOBECODEBANC', 'ABCC'))
