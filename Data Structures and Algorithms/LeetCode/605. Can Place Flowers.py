class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if i == 0:
                prev = 0
            else:
                prev = flowerbed[i-1]
            if i == len(flowerbed)-1:
                next = 0
            else:
                next = flowerbed[i+1]
            cur = flowerbed[i]
            if prev == 0 and cur == 0 and next == 0:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False
