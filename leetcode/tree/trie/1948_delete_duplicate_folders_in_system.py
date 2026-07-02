# Trie + serialization.
from collections import defaultdict

class Solution:
    def deleteDuplicateFolder(self, paths):
        root = {}
        for path in paths:
            node = root
            for name in path:
                node = node.setdefault(name, {})

        signature_groups = defaultdict(list)

        def serialize(node):
            if not node:
                return ""
            parts = []
            for name in sorted(node):
                parts.append(name + "(" + serialize(node[name]) + ")")
            sig = "".join(parts)
            signature_groups[sig].append(node)
            return sig

        serialize(root)

        deleted = set()
        for sig, nodes in signature_groups.items():
            if len(nodes) > 1:
                for node in nodes:
                    deleted.add(id(node))

        res = []

        def collect(node, path):
            for name, child in node.items():
                if id(child) in deleted:
                    continue
                new_path = path + [name]
                res.append(new_path)
                collect(child, new_path)

        collect(root, [])
        return res
