class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j:
                    total += mat[i][j]
                if len(mat)-i - 1 == j:
                    total += mat[i][j]
        if len(mat) % 2 != 0:
            total -= mat[len(mat)//2][len(mat)//2]
        return total
