class Solution:
    def reverseVowels(self, s: str) -> str:

        left = 0
        right = len(s)-1
        vowels = ("a", "e", "i", "o", "u")
        output = ""
        hashmap = {}
        while left <= right:
            if s[left].lower() not in vowels:
                left += 1
                continue
            if s[right].lower() not in vowels:
                right -= 1
                continue
            if s[left].lower() and s[right].lower() in vowels:
                hashmap[left] = s[right]
                hashmap[right] = s[left]
                left += 1
                right -= 1
        for i in range(len(s)):
            if i not in hashmap.keys():
                output = output+s[i]
            else:
                output = output+hashmap[i]
        return output

    # You can also store s in a list and then swap the vowels.


class Solution:
    def reverseVowels(self, s: str) -> str:

        left = 0
        right = len(s)-1
        vowels = ("a", "e", "i", "o", "u")
        output = list(s)
        while left <= right:
            if s[left].lower() not in vowels:
                left += 1
                continue
            if s[right].lower() not in vowels:
                right -= 1
                continue
            if s[left].lower() and s[right].lower() in vowels:
                output[left], output[right] = output[right], output[left]
                left += 1
                right -= 1

        return "".join(output)
