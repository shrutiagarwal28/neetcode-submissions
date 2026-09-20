class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix[0])
        n = len(matrix)
        row = [False] * n
        col = [False] * m

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j] = 0

        