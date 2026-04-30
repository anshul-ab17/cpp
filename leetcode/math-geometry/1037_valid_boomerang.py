class Solution:
    def isBoomerang(self, points):
        a,b,c = points
        return (b[1]-a[1])*(c[0]-a[0]) != (c[1]-a[1])*(b[0]-a[0])
