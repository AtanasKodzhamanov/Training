class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        types = {}
        left = 0
        maxpicked = 0
        picked = 0
        for i in range(len(fruits)):
            types[fruits[i]] = types.get(fruits[i], 0)+1

            while len(types) > 2:
                types[fruits[left]] -= 1
                if types[fruits[left]] == 0:
                    types.pop(fruits[left])
                left += 1

            picked = i-left+1
            maxpicked = max(maxpicked, picked)

        return maxpicked
