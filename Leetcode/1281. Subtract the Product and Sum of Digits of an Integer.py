class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_of_digits = 0
        product_of_digits = 1

        while n:
            last_digit = n % 10
            sum_of_digits += last_digit
            product_of_digits *= last_digit
            n = n // 10

        return product_of_digits - sum_of_digits