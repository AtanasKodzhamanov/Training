class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left, right = 0, len(people)-1
        boats = 0
        while left <= right:
            curboat = 0
            if curboat+people[right] <= limit:
                curboat += people[right]
            if curboat+people[left] <= limit:
                curboat += people[left]
                left += 1
            right -= 1
            boats += 1
        return boats
