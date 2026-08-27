class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        # do sum total of all shifts, and then do the final shift

        direction = 0
        count = 0

        for arrow, num in shift:
            if arrow == 0:

                count -= num
            else:
                count += num
        
        if count < 0:
            direction = 0
        else:
            direction = 1
            
                
        s2 = deque(s)

        if direction == 0:
            while count != 0:
                l_char = s2.popleft()
                s2.append(l_char)
                count += 1
        else:
            while count != 0:
                r_char = s2.pop()
                s2.appendleft(r_char)
                count -= 1

        return "".join(s2)