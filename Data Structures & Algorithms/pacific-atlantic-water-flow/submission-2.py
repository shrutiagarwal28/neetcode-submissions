class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl = set()
        pac = set()
        visited = set()
        res = []

        def dfs(i,j, prev_height, ocean):
            
            if not (0 <= i< len(heights)) or not (0 <= j < len(heights[0])) or (i,j) in ocean or heights[i][j] < prev_height:
               return
            # print(i, j, heights[i][j])
            # visited.add((i,j))
            ocean.add((i,j))
            dfs(i+1,j, heights[i][j], ocean) 
            dfs(i-1,j, heights[i][j], ocean)
            dfs(i,j+1, heights[i][j], ocean)
            dfs(i,j-1, heights[i][j], ocean)
            
        
        for i in range(len(heights)):
            dfs(i, 0, heights[i][0], pac)
            dfs(i, len(heights[0])-1, heights[i][len(heights[0])-1],atl)

        for j in range(len(heights[0])):
            dfs(0, j, heights[0][j] , pac)
            dfs(len(heights)-1, j, heights[-1][j], atl)

        # print(pac)
        # print(atl)
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res

