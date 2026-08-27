class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        # do sum total of all shifts, and then do the final shift

        count = 0
        res = ""

        for arrow, num in shift:
            if arrow == 0:

                count -= num
            else:
                count += num
        print(count)    
        count = (-count) % len(s)
        print(count)

        
        res = s[count:] + s[:count]
        

        return res