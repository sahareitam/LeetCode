class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.adj = {}
        self.end = False


class Trie(object):
    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c in node.adj:
                node = node.adj[c]
            else:
                node.adj[c] = Node(c)
                node = node.adj[c]
        node.end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c in node.adj:
                node = node.adj[c]
            else:
                return False
        return node.end == True

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for p in prefix:
            if p in node.adj:
                node = node.adj[p]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)