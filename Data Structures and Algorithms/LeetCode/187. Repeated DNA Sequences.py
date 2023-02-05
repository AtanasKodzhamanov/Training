class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left = 0
        right = 9
        hashset = set()
        output = set()
        while right < len(s):
            if s[left:right+1] not in hashset:
                hashset.add(s[left:right+1])
            else:
                output.add(s[left:right+1])
            right += 1
            left += 1
        return output

# One complication: instead of neededing 8 bits we can map ACGT to 2 bits. This makes each 10 char subsequnece to be 20bits character instead of 80 bits (10x8).
