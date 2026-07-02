# Hard: DFS with previous operand tracking.
class Solution:
    def addOperators(self, num, target):
        res = []
        n = len(num)

        def dfs(index, path, value, prev):
            if index == n:
                if value == target:
                    res.append(path)
                return
            for i in range(index, n):
                cur_str = num[index:i + 1]
                if len(cur_str) > 1 and cur_str[0] == '0':
                    break
                cur = int(cur_str)
                if index == 0:
                    dfs(i + 1, cur_str, cur, cur)
                else:
                    dfs(i + 1, path + '+' + cur_str, value + cur, cur)
                    dfs(i + 1, path + '-' + cur_str, value - cur, -cur)
                    dfs(i + 1, path + '*' + cur_str, value - prev + prev * cur, prev * cur)

        dfs(0, "", 0, 0)
        return res
