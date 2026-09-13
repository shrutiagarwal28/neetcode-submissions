class TreeNode:
    def __init__(self, val = "") -> None:
        self.val = val
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root 

        for c in word:
            if c not in curr.children:
                node = TreeNode(c)
                curr.children[c] = node
            # print(curr.children, curr)
            curr = curr.children[c]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        
        if curr.endOfWord:return True
        else: return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        
        return True
        