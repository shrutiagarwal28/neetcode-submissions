class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        # do sum total of all shifts, and then do the final shift

        direction = 0
        count = 0
        res = ""

        for arrow, num in shift:
            if arrow == 0:

                count -= num
            else:
                count += num
        
        if count < 0:
            direction = 0
        else:
            direction = 1
            
        count = count % len(s)

        if count < 0:
            res = s[count:] + s[:count]
        else:
            res = s[len(s)-count:] + s[:len(s)-count]

        return res