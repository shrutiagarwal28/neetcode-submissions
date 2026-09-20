class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m
        l, r = 0, n
        res = []

        while l < r and top < bottom:
            
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][r-1])
            r -= 1

            if top >= bottom or l >= r:
                break

            for i in range(r-1, l-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            for j in range(bottom-1, top-1, -1):
                res.append(matrix[j][l])
            l += 1

            # print(l,r,top, bottom)

        return res

