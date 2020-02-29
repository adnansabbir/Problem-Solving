from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        total_profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price

            if price > min_price:
                total_profit += price - min_price
                min_price = price

        return total_profit


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
