from collections import deque


# Used deque instead of List as deque is faster than List by performance


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        parentheses = {
            "opening": ['(', '{', '['],
            "closing_pair": {
                ")": '(',
                "}": '{',
                "]": '[',
            }
        }

        for char in s:
            if char in parentheses["opening"]:
                stack.append(char)
            elif char in parentheses['closing_pair'] and stack:
                if not stack.pop() == parentheses['closing_pair'][char]:
                    return False
            else:
                return False

        return False if stack else True


solution = Solution()
print(solution.isValid("()"))
# TimeComplexity -> O(n)
