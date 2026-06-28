from collections import deque, defaultdict

def generateSchedule(numTasks: int, prerequisites: list[list[int]]) -> list[int]:
    # Topological sort based scheduling (Kahn's Algorithm)
    adj = defaultdict(list)
    in_degree = [0] * numTasks
    
    for u, v in prerequisites:
        adj[u].append(v)
        in_degree[v] += 1
        
    queue = deque([i for i in range(numTasks) if in_degree[i] == 0])
    schedule = []
    
    while queue:
        curr = queue.popleft()
        schedule.append(curr)
        for neighbor in adj[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    if len(schedule) == numTasks:
        return schedule
    return []  # Return empty list if a cycle is detected (impossible schedule)
