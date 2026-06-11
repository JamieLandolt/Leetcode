# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.equal(root.left, root.right)

    def equal(self, l, r):
        if l == None and r == None:
            return True
        if l == None or r == None:
            return False
        if l.val == r.val:
            return self.equal(l.left, r.right) and self.equal(l.right, r.left)
        return False
