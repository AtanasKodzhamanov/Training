class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ctext = Counter(text)
        balloon = Counter("balloon")

        result = float("inf")

        for c in balloon:
            result = min(result, ctext[c]//balloon[c])

        return result


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = {}
        for char in text:
            if char in "balloon":
                hashmap[char] = 1 + hashmap.get(char, 0)
        hashmap["l"] = hashmap.get("l", 0)//2
        hashmap["o"] = hashmap.get("o", 0)//2
        if len(hashmap) != 5:
            return 0
        return min(hashmap.values())
