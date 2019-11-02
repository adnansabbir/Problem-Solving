class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Edge Case
        # Negative numbers cannot be palindrome as it has '-' at beginning
        # Numbers multiple of 10 cannot be palindrome
        # O is a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_x = 0

        # Instead of converting to string and checking as it was the requirement
        while x > reverted_x:
            # Appending the last number of x to reverted_x
            reverted_x = (reverted_x * 10) + (x % 10)
            # Removing last number from x
            x //= 10

        # Now we have half the number in x and other half at reversed_x
        # If reverted_x has 1 more digit it wont be counted as the middle value of Ok for palindrome
        return x == reverted_x or x == reverted_x // 10


solution = Solution()
print(solution.isPalindrome(121))
# RunTime - > O(log10(n)) as we are dividing x by 10 each iteration