class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Can use formula row/2*(row+1) which gives the sum of a sequence
        # This works here because each row contains the same number of coins as the number of the row.
        # So a pyramid of size 3 will contain 1+2+3 coins. Applying the formula to n can tell us how many coins a pyramid of size "row" requires
        # We are going to start from assuming a certain number of rows and

        # return int((math.sqrt(1 + 8 * n) - 1) / 2)
        left = 1
        right = n
        coins = 0
        res = 0
        while left <= right:
            middle = (left+right)//2
            coins = int(middle/2*(middle+1))
            if coins > n:
                right = middle-1
            else:
                left = middle+1
                res = max(middle, res)
        return res
