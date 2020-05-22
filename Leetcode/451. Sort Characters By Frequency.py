import operator


class Solution:
    def frequencySort(self, s: str) -> str:
        frequency_array = [[0, 0, 0] for j in range(123)]
        for pos, char in enumerate(s):
            index = ord(char)

            if frequency_array[index][0]:
                frequency_array[index][0] += 1
            else:
                frequency_array[index] = [1, pos, char]

        sorted_frequency = sorted(frequency_array, key=operator.itemgetter(0, 1))
        new_string = ''

        for freq in sorted_frequency[::-1]:
            if not freq[0]:
                return new_string
            else:
                new_string += freq[2] * (freq[0])

        return new_string


sol = Solution()
print(sol.frequencySort('tree'))