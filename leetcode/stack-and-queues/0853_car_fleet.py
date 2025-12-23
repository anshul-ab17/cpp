class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        cur = 0
        for p, s in cars:
            t = (target - p) / s
            if t > cur:
                fleets += 1
                cur = t
        return fleets
