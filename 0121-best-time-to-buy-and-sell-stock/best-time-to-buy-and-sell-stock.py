class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        minprice = float('inf')


        for price in prices:
            if price < minprice:
                minprice = price
            if price - minprice > maxprofit:
                maxprofit = price - minprice
        return maxprofit

        