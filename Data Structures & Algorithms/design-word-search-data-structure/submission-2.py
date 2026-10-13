class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for l in word:
            if l not in cur.children:
                cur.children[l] = TrieNode()
            cur = cur.children[l]
        cur.word = True
        

    def search(self, word: str) -> bool:
        d = deque()
        d.append(self.root)
        for l in word:
            if not d:
                return False
            for i in range(len(d)):
                cur = d.popleft()
                if l == '.':
                    for v in cur.children:
                        d.append(cur.children[v])
                elif l in cur.children:
                    d.append(cur.children[l])
                                    
            
        for i in range(len(d)):
            cur = d.popleft()
            if cur.word:
                return True
        return False
