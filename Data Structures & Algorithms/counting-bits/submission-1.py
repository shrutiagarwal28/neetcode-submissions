class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            ones = 0

            while i:
                if i & 1:
                    ones += 1
                i >>= 1
            res.append(ones)

            # while n:
            # res += 1 if n & 1 else 0
            # n >>= 1
        return res