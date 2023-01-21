class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ctext = Counter(text)
        balloon = Counter("balloon")

        result = float("inf")

        for c in balloon:
            result = min(result, ctext[c]//balloon[c])

        return result
