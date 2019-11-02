class Solution:
    def romanToInt(self, s: str) -> int:
        roman_letter = {
            " ": 0,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        s += ' '
        for i, ch in enumerate(s[:-1]):
            value = roman_letter[ch]
            next_value = roman_letter[s[i + 1]]

            # If value is >= next value we will add the number or we reduce it
            total += value if value >= next_value else -value

        return total


solution = Solution()
print(solution.romanToInt("IV"))
