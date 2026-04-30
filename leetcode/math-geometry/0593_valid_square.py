class Solution:
    def validSquare(self, p1, p2, p3, p4):
        pts = [p1,p2,p3,p4]

        def dist(a,b):
            return (a[0]-b[0])**2 + (a[1]-b[1])**2

        s = sorted(dist(pts[i], pts[j]) for i in range(4) for j in range(i+1,4))
        return s[0] > 0 and s[0]==s[1]==s[2]==s[3] and s[4]==s[5]
