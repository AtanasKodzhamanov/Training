from http.client import UnimplementedFileMode
from pickle import FALSE
from turtle import left, right

from numpy import False_

# ugly but comprehensible 
def numCells(grid):
    output=0
    for r in range(0,len(grid)):
        for c in range(0,len(grid[0])):     
            num=grid[r][c]
            count=0
            if c-1>=0:
                if num<=grid[r][c-1]:
                    count+=1
            if c+1<len(grid[0]):
                if num<=grid[r][c+1]:
                    count+=1
            if r-1>=0:
                if num<=grid[r-1][c]:
                    count+=1
            if r+1<len(grid):
                if num<=grid[r+1][c]:
                    count+=1
            if r+1<len(grid) and c+1<len(grid[0]):
                if num<=grid[r+1][c+1]:
                    count+=1
            if r+1<len(grid) and c-1>=0:
                if num<=grid[r+1][c-1]:
                    count+=1
            if r-1>=0 and c+1<len(grid[0]):
                if num<=grid[r-1][c+1]:
                    count+=1        
            if r-1>=0 and c-1>=0:
                if num<=grid[r-1][c-1]:
                    count+=1
            if count==0:
                output+=1
    return output

numCells([[1, 2, 7], [4, 5, 6], [8, 8, 9]])
