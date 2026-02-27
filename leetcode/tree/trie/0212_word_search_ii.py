# LC 212. Word Search II | Hard
class Solution:
    def findWords(self, board, words):
        trie = {}
        for w in words:
            node = trie
            for ch in w: node = node.setdefault(ch, {})
            node['$'] = w
        m, n = len(board), len(board[0]); res = []
        def dfs(i, j, node):
            ch = board[i][j]
            if ch not in node: return
            node = node[ch]
            if '$' in node: res.append(node.pop('$'))
            board[i][j] = '#'
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    dfs(ni, nj, node)
            board[i][j] = ch
        for i in range(m):
            for j in range(n): dfs(i, j, trie)
        return res
