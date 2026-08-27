class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotatable_nos = {0:0, 1:1, 6:9, 8:8, 9:6}
        reverse_num = []

        for num in str(n):
            if int(num) not in rotatable_nos:
                return False
            reverse_num.append(str(rotatable_nos[int(num)]))
        
        reverse_num.reverse()
        return not n == int("".join(reverse_num))