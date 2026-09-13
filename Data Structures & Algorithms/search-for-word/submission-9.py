class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(i,j, idx):
           
            if idx == len(word):
                return True
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0]))  or board[i][j] != word[idx] or (i,j) in visited:
               
                return False
            
            visited.add((i,j))
            
            isHere = ( dfs(i+1, j, idx+1) or 
            dfs(i-1, j, idx+1) or
            dfs(i, j+1, idx+1) or
            dfs(i,j-1, idx+1) )
            
            visited.remove((i,j))
                
            return isHere
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j, 0):
                        return True
        
        return False

        # T.C. : m × n  ×  4^L