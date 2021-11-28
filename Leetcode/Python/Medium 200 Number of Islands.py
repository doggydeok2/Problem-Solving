class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dxy = [0, 1, 0, -1, 0]
        
        
        def island_checking(y, x):
            grid[y][x] = "0"
            for k in range(4):
                ty, tx = y + dxy[k], x + dxy[k + 1]
                if 0 <= ty < m and 0 <= tx < n and grid[ty][tx] == "1":
                    island_checking(ty, tx)
        
        
        m, n, cnt = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    island_checking(i, j)
                    
        return cnt
