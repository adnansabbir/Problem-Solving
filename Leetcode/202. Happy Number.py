class Solution:
    def isHappy(self, n: int, number_set=None) -> bool:
        number_set = {4, 20, 37, 89}
        while n != 1:
            if n in number_set:
                return False

            num_str = str(n)
            new_num = 0
            for digit in num_str:
                new_num += int(digit) * int(digit)
            n = new_num

        return True


class Solution2:
    def isHappy(self, n: int, number_set=None) -> bool:
        number_set = {4, 20, 37, 89}
        while n != 1:
            if n in number_set:
                return False

            num_str = str(n)
            new_num = 0
            for digit in num_str:
                new_num += int(digit) * int(digit)
            n = new_num

        return True


class Solution3:
    def digit_sum(self, n):
        sum_digit_square = 0

        while n > 0:
            digit = n % 10
            sum_digit_square += digit ** 2
            n = n // 10

        return sum_digit_square

    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = self.digit_sum(slow)

            fast = self.digit_sum(fast)
            fast = self.digit_sum(fast)

            if slow == 1 or fast == 1:
                return True

            if slow == fast:
                return False


sol = Solution2()
arr = []
for i in range(1, 101):
    if sol.isHappy(i):
        arr.append(i)

print(arr)
