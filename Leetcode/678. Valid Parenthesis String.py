class Solution:
    def checkValidString(self, s: str) -> bool:
        open = 0

        for char in s:
            if char == "(" or char == "*":
                open += 1
            else:
                open -= 1
            if open < 0:
                return False
        if open == 0:
            return True

        closed = 0
        for char in s[::-1]:
            if char == ")" or char == "*":
                closed += 1
            else:
                closed -= 1
            if closed < 0:
                return False

        return True


sol = Solution()
print(sol.checkValidString("()*)(*)"))
