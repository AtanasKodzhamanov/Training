class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        hashtable1 = {}
        hashtable2 = {}
        for i in range(len(pattern)):
            if hashtable1.get(pattern[i]):
                if not hashtable1[pattern[i]] == words[i]:
                    return False
            else:
                hashtable1[pattern[i]] = words[i]
            if hashtable2.get(words[i]):
                if not hashtable2[words[i]] == pattern[i]:
                    return False
            else:
                hashtable2[words[i]] = pattern[i]
        return True


# neater solution
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        charToWord = {}
        wordToChar = {}

        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
        return True


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_index = {}
        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(words)):
            c = pattern[i]
            w = words[i]

            char_key = 'char_{}'.format(c)
            char_word = 'word_{}'.format(w)

            if char_key not in map_index:
                map_index[char_key] = i

            if char_word not in map_index:
                map_index[char_word] = i

            if map_index[char_key] != map_index[char_word]:
                return False

        return True
