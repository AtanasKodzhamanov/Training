class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            # n is shifted to the right by 1 using the bitwise right shift operator (>>). This discards the least significant bit and moves all the other bits one place to the right.
            n = n >> 1
        return res

        # O(32) constant so O(1). The problem is that we have to look at each number even if its 0. There is an alternative solution that is faster
