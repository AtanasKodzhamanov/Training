class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mind = 100000
        profit = 0
        for i in range(len(prices)):
            if prices[i] < mind:
                mind = prices[i]
            profit = max(prices[i]-mind, profit)
        return profit

    # What we are doing here is simply keeping track of the minimum price we have seen so far and the maximum profit we can make.
