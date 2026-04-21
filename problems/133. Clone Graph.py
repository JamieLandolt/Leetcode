# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        # Make copies
        node_clones = {}
        self.cloneAllNodes(node, node_clones)

        for clone in node_clones.values():
            clone.neighbors = [node_clones[nb.val] for nb in clone.neighbors]

        return node_clones[node.val]

    def cloneAllNodes(self, node, node_clones):
        # Clone all nodes
        node_clones[node.val] = Node(node.val, node.neighbors)
        for nb in node.neighbors:
            if nb.val not in node_clones:
                self.cloneAllNodes(nb, node_clones)