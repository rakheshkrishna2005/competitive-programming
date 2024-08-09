class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(i: int, j: int) -> bool:

            s = ""
            indices = [0, 1, 2, 5, 8, 7, 6, 3]
            
            for num in indices:
                row = i + num // 3
                col = j + num % 3
                s += str(grid[row][col])

            return s in "4381672943816729" or s in "4381672943816729"[::-1]

        res = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows - 2):
            for j in range(cols - 2):
                if grid[i][j] % 2 == 0 and grid[i + 1][j + 1] == 5:
                    if check(i, j):
                        res += 1

        return res
