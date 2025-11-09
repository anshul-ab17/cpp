# LC 297. Serialize and Deserialize Binary Tree | Hard | Google
class TreeNode:
    def __init__(self, x): self.val = x; self.left = self.right = None

class Codec:
    def serialize(self, root):
        res = []
        def pre(node):
            if not node: res.append('N'); return
            res.append(str(node.val)); pre(node.left); pre(node.right)
        pre(root); return ','.join(res)

    def deserialize(self, data):
        vals = iter(data.split(','))
        def build():
            v = next(vals)
            if v == 'N': return None
            node = TreeNode(int(v)); node.left = build(); node.right = build()
            return node
        return build()
