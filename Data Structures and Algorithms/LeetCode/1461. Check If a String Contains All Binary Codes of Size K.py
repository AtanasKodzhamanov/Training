class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        total = 2**k
        output = set()
        for i in range(len(s)-k+1):
            curr = s[i:i+k]
            output.add(curr)
        return len(output) == total
