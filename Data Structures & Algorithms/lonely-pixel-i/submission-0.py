class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row_counts = [0 for r in range(len(picture))]
        col_counts = [0 for c in range(len(picture[0]))]
        count = 0

        for r in range(len(picture)):
            for c in range(len(picture[0])):
                if picture[r][c] == "B":
                    row_counts[r] += 1
                    col_counts[c] += 1
        
        for r in range(len(picture)):
            for c in range(len(picture[0])):
                if picture[r][c] == "B" and row_counts[r] == 1 and col_counts[c] == 1:
                    count += 1
        
        return count