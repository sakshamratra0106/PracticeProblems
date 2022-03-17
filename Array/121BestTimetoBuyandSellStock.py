from typing import List


class Solution:

    def __init__(self, prices: List[int]):
        self.prices = prices

    def showPrices(self):
        return self.prices

    def maxProfit(self) -> int:
        # Since we want a number which is least in number in later part of the code
        # we are using the max of the integer
        leastPriceSoFar = max(self.prices)
        maxProfit = 0
        for todayPrice in self.prices:
            if todayPrice < leastPriceSoFar:
                leastPriceSoFar = todayPrice
            elif maxProfit < todayPrice - leastPriceSoFar:
                maxProfit = todayPrice - leastPriceSoFar

            # print(todayPrice,"--",leastPriceSoFar,"--",maxProfit)
            # UnComment above code for debugging
        return maxProfit


if __name__ == "__main__":
    sol1 = Solution([7, 1, 5, 3, 6, 4])
    print("Maximum profit out of Stock prices which is : {} would have been : {}"
          .format(sol1.showPrices(), sol1.maxProfit()))
    sol2 = Solution([7,6,4,3,1])
    print("Maximum profit out of Stock prices which is : {} would have been : {}"
          .format(sol2.showPrices(), sol2.maxProfit()))
