class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        l, r, boats = 0, len(people)-1, 0
        while l <= r:
            if people[l] + people[r] <= limit: l += 1
            r -= 1; boats += 1
        return boats
