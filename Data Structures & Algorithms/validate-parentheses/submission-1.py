class Solution:
    def isValid(self, s: str) -> bool:
        opening_para = []
        para_dict = {")":"(", "}":"{", "]":"["}
        i = 0

        while i < len(s):
            if s[i] in "[{(":
                opening_para.append(s[i])
                i+=1
            else:
                if opening_para and s[i] in para_dict:
                    top = opening_para.pop()
                    if top != para_dict[s[i]]:
                        return False
                    i += 1
                else:
                    return False
        
        if opening_para : return False
        return True