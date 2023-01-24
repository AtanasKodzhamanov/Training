class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        width=sum(wall[0])
        height=len(wall)

        hashtable={0:0} # so that max(hashtable.values()) works when its empty
        for r in range(height):
            cumsum=0
            for i in range(len(wall[r])):
                cumsum+=wall[r][i]
                if cumsum== width:
                    continue
                hashtable[cumsum]= 1 +hashtable.get(cumsum,0)
                
        gaps=max(hashtable.values())
        return height-gaps
