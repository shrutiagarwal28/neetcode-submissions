class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        n = len(picture)
        m = len(picture[0])

        # Arrays to store the count of black cells in rows and columns.
        row_count = [0] * n
        column_count = [0] * m
        for i in range(n):
            for j in range(m):
                if picture[i][j] == 'B':
                    row_count[i] += 1
                    column_count[j] += 1

        answer = 0
        for i in range(n):
            for j in range(m):
                # Its a lonely cell, if the current cell is black and,
                # the count of black cells in its row and column is 1.
                if picture[i][j] == 'B' and row_count[i] == 1 and column_count[j] == 1:
                    answer += 1

        return answer
        