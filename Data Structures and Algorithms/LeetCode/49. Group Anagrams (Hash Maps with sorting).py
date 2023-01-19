import collections


class Solution(object):
    def groupAnagrams(self, strs):
        # Create a dictionary with a list as a value
        output = collections.defaultdict(list)
        for s in strs:
            # Sort each string and use it as a key in a dictionary
            output[tuple(sorted(s))].append(s)
        return output.values()
