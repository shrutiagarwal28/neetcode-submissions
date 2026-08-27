class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]

        for row_idx, row_elements in enumerate(mat1):
            for ele_idx, ele in enumerate(row_elements):
                if ele:
                    for col_idx, col_ele in enumerate(mat2[ele_idx]):
                        ans[row_idx][col_idx] += ele * col_ele
        return ans