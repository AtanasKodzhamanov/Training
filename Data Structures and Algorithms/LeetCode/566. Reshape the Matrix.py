class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        size = len(mat)*len(mat[0])
        matrix = [[0 for j in range(c)] for i in range(r)]
        if size != r*c:
            return mat
        countc = 0
        countr = 0
        for i in mat:
            for j in i:
                if countc == c:
                    countc = 0
                    countr += 1
                matrix[countr][countc] = j
                countc += 1
        return matrix
