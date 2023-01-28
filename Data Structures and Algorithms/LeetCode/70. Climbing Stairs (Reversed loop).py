class Solution:
    def climbStairs(self, n: int) -> int:
        # first and second and the final two steps where it takes only 1 step to reach n
        first, second = 1, 1

        for i in range(n-1):
            # keep shifting first and second keeping a cumulative sum
            temp = first
            first = first + second
            second = temp

        return first

# the idea is to start from the end and work backwards to the beginning
# we know that n and n-1 are the final two steps where it takes only 1 step to reach n
# then at n-2 we can take 1 step to reach n-1 or 2 steps to reach n. The total number of ways to reach n is the sum of the number of ways to reach n-1 and n. We can keep shifting first and second keeping a cumulative sum and return first at the end of the loop.
