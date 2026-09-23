class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = collections.defaultdict(set)
        col_map = collections.defaultdict(set)
        box_map = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] in row_map[i] or board[i][j] in col_map[j] or board[i][j] in box_map[(i//3, j//3)]:
                    # print
                    return False
                if board[i][j] != ".":
                    row_map[i].add(board[i][j])
                    col_map[j].add(board[i][j])
                    box_map[(i//3, j//3)].add(board[i][j])
        
        return True