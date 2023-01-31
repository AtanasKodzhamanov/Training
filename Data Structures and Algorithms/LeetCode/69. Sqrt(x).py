class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        while left <= right:
            middle = (left+right)//2
            sqr = middle**2

            if sqr == x:
                return middle
            if sqr < x:
                left = middle+1
            else:
                right = middle-1

        return right


s = Solution()
result = s.mySqrt(8)
