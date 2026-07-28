# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root, num="1000"):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        l = self.serialize(root.left)
        r = self.serialize(root.right)
        return f"({len(str(root.val))}){root.val}({len(l)}){l}({len(r)}){r}"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        if data.isdigit():
            return TreeNode(int(data), None, None)

        root_val, left, right = self.parse(data)
        root = TreeNode(root_val, self.deserialize(left), self.deserialize(right))
        return root

    def parse(self, data):
        rb = data.find(")")
        root_len = int(data[1:rb])
        root_val = int(data[rb + 1:rb + 1 + root_len])

        lb_2 = data.find("(", 1)
        rb_2 = data.find(")", lb_2)
        left_len = int(data[lb_2 + 1:rb_2])
        left_val = data[rb_2 + 1:rb_2 + 1 + left_len]

        lb_3 = rb_2 + 1 + left_len
        rb_3 = data.find(")", lb_3)
        right_len = int(data[lb_3 + 1:rb_3])
        right_val = data[rb_3 + 1:rb_3 + 1 + right_len]

        return root_val, left_val, right_val

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))