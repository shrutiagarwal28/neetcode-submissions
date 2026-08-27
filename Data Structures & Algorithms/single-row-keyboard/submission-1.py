class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key_map = {}
        for i, val in enumerate(keyboard):
            key_map[val] = i
        time = 0
        pos = 0
        for char in word:
            time += abs(pos - key_map[char])
            pos = key_map[char]
        return time