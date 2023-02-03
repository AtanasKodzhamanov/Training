class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            middle = (left+right)//2
            sqr = middle**2

            if sqr == num:
                return True
            if sqr < num:
                left = middle+1
            else:
                right = middle-1

        return False
