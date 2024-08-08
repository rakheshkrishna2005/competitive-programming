class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        result = []
        r, c = rStart, cStart
        steps = 1
        direction = 0

        while len(result) < rows * cols:
            for _ in range(2):
                dr, dc = directions[direction]
                for _ in range (steps):
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                    r, c = r + dr, c + dc 

                direction = (direction + 1) % 4
                
            steps += 1

        return result
