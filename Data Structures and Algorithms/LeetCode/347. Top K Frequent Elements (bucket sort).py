class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = [[] for i in range(len(nums)+1)]

        countDict = Counter(nums)
        result = []
        for value, count in countDict.items():
            output[count].append(value)

        for i in range(len(output)-1, -1, -1):
            for j in output[i]:
                if k == 0:
                    return result
                result.append(j)
                k -= 1
        return result
        # we take the count of the numbers and create a dictionary countDict
        # we create an emtpy list of lenght nums+1 that contains lists
        # in this empty array we map the frequency to be equal to the index of the array
        # so we take the count value of the dictionary and map the key to the index
