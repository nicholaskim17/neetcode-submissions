class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cheapest_buy = prices[0]

        for i in range(1, len(prices)):
            #looping thorugh selling prices

            if prices[i] - cheapest_buy > max_profit:
                max_profit = prices[i] - cheapest_buy
            #checking if current sell is best profit

            if prices[i] < cheapest_buy:
                cheapest_buy = prices[i]

        return max_profit


