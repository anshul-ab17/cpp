# DSU on account indices + email mapping.
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb

class Solution:
    def accountsMerge(self, accounts):
        dsu = DSU(len(accounts))
        email_to_acc = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_acc:
                    dsu.union(i, email_to_acc[email])
                else:
                    email_to_acc[email] = i

        groups = {}
        for email, i in email_to_acc.items():
            root = dsu.find(i)
            groups.setdefault(root, set()).add(email)

        res = []
        for root, emails in groups.items():
            res.append([accounts[root][0]] + sorted(emails))

        return res
