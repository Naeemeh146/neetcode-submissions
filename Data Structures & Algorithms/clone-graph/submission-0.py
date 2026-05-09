"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        old_to_new = {}

        def clone(node):

            if node in old_to_new:
                return old_to_new[node]

            newnode = Node(node.val)

            old_to_new[node] = newnode

            for nei in node.neighbors:
                newnode.neighbors.append(clone(nei))

            return newnode

        return clone(node) if node else node