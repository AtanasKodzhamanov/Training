
# n!/(n-k)!k! - number of k combinations out of n
# can use value*(value-1)//2 as a formula

class Solution:
    def calc(self, number):
        total = 0

        while number > 0:
            total = number-1+total
            number -= 1

        return total

    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hashmap = {}
        pairs = 0

        for i in rectangles:
            hashmap[i[0]/i[1]] = 1+hashmap.get(i[0]/i[1], 0)

        for value in hashmap.values():
            pairs = pairs+self.calc(value)

        return pairs
