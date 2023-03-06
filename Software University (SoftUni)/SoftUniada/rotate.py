
n = int(input())
matrix = []
rotated_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    row = input().split()
    row = [int(num) for num in row]
    matrix.append(row)

for i in range(n):
    for j in range(n):
        rotated_matrix[j][n-i-1] = matrix[i][j]

for row in rotated_matrix:
    print(" ".join(str(num) for num in row))
