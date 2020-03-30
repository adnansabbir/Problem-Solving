import collections


class HashSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_hash = {}

        for char in s:
            if char not in char_hash:
                char_hash[char] = 1
            else:
                char_hash[char] += 1

        for char in t:
            if char not in char_hash or not char_hash[char]:
                return False
            else:
                char_hash[char] -= 1

        return True


# sol = HashSolution()
# print(sol.isAnagram('anagram', 'nagaram'))

class HashSolutionWithCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return collections.Counter(list(s)) == collections.Counter(list(t))


class ArraySolution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26

        for char in s:
            arr[ord(char) - 97] += 1

        for char in t:
            if arr[ord(char) - 97] == 0:
                return False
            else:
                arr[ord(char) - 97] -= 1

        return len(s) == len(t)

# print(ord('z'))
