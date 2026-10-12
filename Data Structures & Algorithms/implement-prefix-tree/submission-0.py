class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if not word:
            return
        cur = self.root
        for l in word:
            if l not in cur.children:
                cur.children[l] = TrieNode()
            cur = cur.children[l]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for l in word:
            if l not in cur.children:
                return False
            cur = cur.children[l]
        return cur.word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for l in prefix:
            if l not in cur.children:
                return False
            cur = cur.children[l]
        return True
        