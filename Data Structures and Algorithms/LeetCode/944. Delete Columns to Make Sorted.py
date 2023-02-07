class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete = 0
        columns = len(strs[0])
        for i in range(columns):
            prev = ""
            for j in range(len(strs)):
                if strs[j][i] >= prev:
                    prev = strs[j][i]
                else:
                    delete += 1
                    break

        return delete
