from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = max(prices)
        globalMaxProfit = 0
        maxProfit = 0

        for index, price in enumerate(prices):

            # This if is to all the profit we can earn and add into globalMaxProfit
            if maxProfit > price - minPrice:
                minPrice = price
                globalMaxProfit += maxProfit
                maxProfit = 0

            # Below two elif is similar to the problem statement
            # where we just buy once and sell once
            elif price < minPrice:
                minPrice = price

            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice

        # including last maxProfit for the last increasing trend
        return globalMaxProfit + maxProfit


if __name__ == "__main__":
    sharePrices = [7, 1, 5, 3, 6, 4]
    print("Maximum profit out of Stock prices which are : {} would have been : {}"
          .format(sharePrices, Solution().maxProfit(sharePrices)))

    sharePrices = [1, 2, 3, 4, 5]
    print("Maximum profit out of Stock prices which are : {} would have been : {}"
          .format(sharePrices, Solution().maxProfit(sharePrices)))

    sharePrices = [7, 6, 4, 3, 1]
    print("Maximum profit out of Stock prices which are : {} would have been : {}"
          .format(sharePrices, Solution().maxProfit(sharePrices)))
