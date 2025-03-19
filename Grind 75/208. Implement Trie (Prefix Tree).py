class Node(object):
    def __init__(self):
        self.map = {}
        self.end = False

class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:
            if c in cur.map:
                cur = cur.map[c]
            else:
                cur.map[c] = Node()
                cur = cur.map[c]
        cur.end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if c in cur.map:
                cur = cur.map[c]
            else:
                return False
        return cur.end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in prefix:
            if c in cur.map:
                cur = cur.map[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)