class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        for i in range(len(prices)-1):
            l = i
            r = i+1

            while r<len(prices):
                if prices[r] > prices[l]:
                    max_profit = max(prices[r] - prices[l], max_profit)
                r+=1


        return max_profit




        