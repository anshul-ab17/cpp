class Solution:
    def restoreIpAddresses(self, s):
        ans = []
        def dfs(i, parts):
            if len(parts) == 4 and i == len(s):
                ans.append(".".join(parts)); return
            if len(parts) == 4: return
            for j in range(i, min(i+3, len(s))):
                p = s[i:j+1]
                if (p[0] == '0' and len(p) > 1) or int(p) > 255:
                    continue
                dfs(j+1, parts+[p])
        dfs(0, [])
        return ans
