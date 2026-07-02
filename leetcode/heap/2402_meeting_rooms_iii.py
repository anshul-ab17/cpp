# Use two heaps: available rooms + occupied rooms.
import heapq

class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()
        available = list(range(n))
        heapq.heapify(available)
        busy = []  # (end_time, room)
        count = [0] * n

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(busy, (end_time + (end - start), room))

            count[room] += 1

        return count.index(max(count))
