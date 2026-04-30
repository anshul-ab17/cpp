class Solution:
    def checkStraightLine(self, coords):
        x0,y0 = coords[0]
        x1,y1 = coords[1]

        for x,y in coords[2:]:
            if (y1-y0)*(x-x0) != (y-y0)*(x1-x0):
                return False
        return True
