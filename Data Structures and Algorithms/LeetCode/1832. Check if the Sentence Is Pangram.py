class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        hashset = set(sentence)
        if len(hashset) < 26:
            return False

        return True
