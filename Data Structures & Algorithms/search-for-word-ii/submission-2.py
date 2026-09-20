class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False
        self.word = ""

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                new_node = TrieNode()
                curr.children[c] = new_node
            curr = curr.children[c]
        curr.endOfWord = True
        curr.word = word


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        for word in words:
            self.addWord(word)

        res = []
        root = self.root
        visited = set()

        def dfs(i, j, curr):
            if not(0<=i<len(board)) or not (0<=j<len(board[0])) or (i,j) in visited or board[i][j] not in curr.children:
                return 
            visited.add((i,j))
            curr = curr.children[board[i][j]]
            if curr.endOfWord:
                res.append(curr.word)
                curr.endOfWord = False
                # Once you discover a word at curr, mark curr.endOfWord = False (or set curr.word = None) so subsequent paths hitting the same node won't add duplicates. For a significant speedup (Trie pruning), you can also remove leaf nodes from curr.children once all their sub-words have been found.
            dfs(i+1, j, curr)
            dfs(i-1, j, curr)
            dfs(i, j-1, curr)
            dfs(i, j+1, curr)
            visited.remove((i,j))
            
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root)
                    
        
        return res
