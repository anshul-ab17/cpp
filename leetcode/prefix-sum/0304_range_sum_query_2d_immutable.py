class NumMatrix:
    def __init__(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.pref = [[0]*(COLS+1) for _ in range(ROWS+1)]

        for r in range(ROWS):
            for c in range(COLS):
                self.pref[r+1][c+1] = (
                    matrix[r][c]
                    + self.pref[r][c+1]
                    + self.pref[r+1][c]
                    - self.pref[r][c]
                )

    def sumRegion(self, r1, c1, r2, c2):
        p = self.pref
        return p[r2+1][c2+1] - p[r1][c2+1] - p[r2+1][c1] + p[r1][c1]
