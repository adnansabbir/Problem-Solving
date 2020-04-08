from typing import List


class Solution:
    @staticmethod
    def create_anagram_hash(phrase: str):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        hash_str = 1
        for char in phrase:
            hash_str *= primes[ord(char) - ord('a')]
        return hash_str

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for phrase in strs:
            hash_str = self.create_anagram_hash(phrase)
            if hash_str not in anagram_dict:
                anagram_dict[hash_str] = [phrase]
            else:
                anagram_dict[hash_str].append(phrase)

        anagram_group = [value_list for value_list in anagram_dict.values()]
        # print(anagram_dict)
        return anagram_group


sol = Solution()
# print(sol.sort_alphabets('hello'))
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(sol.sort_alphabets('tana'))
