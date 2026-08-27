class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        word_len = len(words)
        res = []
        max_col_len = 0
        
        for word in words:
            max_col_len = max(len(word), max_col_len)

        if max_col_len != len(words[0]) or word_len != max_col_len:
            return False 

        for c in range(max_col_len):
            new_word = []
            for row in range(word_len):
                if c < len(words[row]):
                    new_word.append(words[row][c])
            res.append(''.join(new_word))

        return words == res