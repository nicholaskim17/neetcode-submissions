class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cheapest_buy = prices[0]
        max_profit = 0


        for i in range(1,len(prices)):
            if prices[i]-cheapest_buy>max_profit:
                max_profit = prices[i]-cheapest_buy

            if prices[i]<cheapest_buy:
                cheapest_buy = prices[i]

        return max_profit

        