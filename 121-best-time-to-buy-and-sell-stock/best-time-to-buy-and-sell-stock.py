class Solution:
    def maxProfit(self, prices: List[int]) -> int: 

        profit = 0
        diff = 0
        minEl = prices[0]
        for el in prices[1:]:
            if el < minEl:
                minEl = el
            else:
                diff = el - minEl
            if profit < diff:
                profit = diff
        return profit
      
        