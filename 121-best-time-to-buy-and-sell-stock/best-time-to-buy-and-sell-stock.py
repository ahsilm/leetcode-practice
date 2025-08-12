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
        # profit = 0
        # for i in range(len(prices)-1):
        #     maxVal = 0
        #     for j in range(i+1, len(prices)):
        #         if prices[j] > maxVal:
        #             maxVal = prices[j]
        #     diff = maxVal - prices[i]
        #     if diff > profit:
        #         profit = diff

        return profit
        # profit = 0
        # for i in range(len(prices)-1):
        #     maxVal = max(prices[i+1:len(prices)])
        #     diff = maxVal - prices[i] 
        #     if diff > profit:
        #         profit = diff
        # return profit 
        # i = 0
        # j = 1
        # diff = 0
        # while( (i < len(prices)-1) and (i < j)):
        #     val = prices[j] - prices[i]
        #     if val > diff:
        #             diff = val
        #     j += 1
        #     if (j == len(prices)):
        #         i += 1
        #         j = i+1

        # return diff

        
        