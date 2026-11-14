class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = float('inf')
        profit = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]

            else:
                profit = max(profit, prices[i] - buy)

        return profit

        #test