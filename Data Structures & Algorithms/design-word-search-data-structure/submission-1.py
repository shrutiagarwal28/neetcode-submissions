class TreeNode:
    def __init__(self) -> None:
        
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        def dfs(idx, root):
            cur = root

            for j in range(idx, len(word)):
                if word[j] == ".":
                    for child in cur.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if word[j] in cur.children:
                        cur = cur.children[word[j]]
                    else:
                        return False
            
            return cur.endOfWord



            return cur.endOfWord
            

        return dfs(0, cur)