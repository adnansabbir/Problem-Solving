import itertools


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S_stack = []
        T_stack = []

        for char in S:
            if char == "#" and S_stack:
                S_stack.pop()
            elif char != '#':
                S_stack.append(char)

        for char in T:
            if char == "#" and T_stack:
                T_stack.pop()
            elif char != '#':
                T_stack.append(char)

        return ''.join(S_stack) == ''.join(T_stack)


class Solution2:
    @staticmethod
    def generate_phrase(phrase):
        skip = 0
        for char in reversed(phrase):
            if char == "#":
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield char

    def backspaceCompare(self, S: str, T: str) -> bool:
        return all([x == y for x, y in itertools.zip_longest(self.generate_phrase(S), self.generate_phrase(T))])


sol = Solution()
print(sol.backspaceCompare("y#ao##f", "y#f#o##f"))
