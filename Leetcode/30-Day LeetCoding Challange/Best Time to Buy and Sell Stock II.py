from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i, price in enumerate(prices[1:]):
            if price - prices[i] > 0:
                max_profit += price - prices[i]

        return max_profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        bought = prices[0]
        last = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price > last:
                last = price
            else:
                max_profit += last - bought
                bought = last = price

        max_profit += last - bought

        return max_profit


sol = Solution2()
print(sol.maxProfit([1, 0, 0, 0, 7, 4]))
