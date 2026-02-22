class Solution:
    def equationsPossible(self, equations):
        dsu = DSU(26)

        for eq in equations:
            if eq[1] == '=':
                dsu.union(ord(eq[0])-97, ord(eq[3])-97)

        for eq in equations:
            if eq[1] == '!':
                if dsu.find(ord(eq[0])-97) == dsu.find(ord(eq[3])-97):
                    return False
        return True
