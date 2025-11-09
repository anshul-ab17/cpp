# LC 1268. Search Suggestions System | Medium | Amazon
class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort(); res = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            matches = [p for p in products if p.startswith(prefix)]
            res.append(matches[:3])
        return res
