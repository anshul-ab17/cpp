class Solution:
    def canVisitAllRooms(self, rooms):
        seen = {0}

        def dfs(room):
            for key in rooms[room]:
                if key not in seen:
                    seen.add(key)
                    dfs(key)

        dfs(0)
        return len(seen) == len(rooms)
