"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        seen = {}
        def dfs(node):
            if node in seen:
                return seen[node]
            copy = Node(node.val)
            seen[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        return dfs(node) if node else None