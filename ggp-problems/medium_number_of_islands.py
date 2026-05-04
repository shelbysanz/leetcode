class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        vis = [[0] * cols for _ in range(rows)]
        island_count = 0

        def dfs(x, y):
            vis[x][y] = 1
            if grid[x][y] == "0":
                return False
            t, b, l, r = (
                max(0, x - 1),
                min(rows - 1, x + 1),
                max(0, y - 1),
                min(y + 1, cols - 1),
            )
            for xi, yi in [(t, y), (b, y), (x, l), (x, r)]:
                if not vis[xi][yi] and grid[xi][yi] == "1":
                    dfs(xi, yi)
            return True

        for row in range(rows):
            for col in range(cols):
                if not vis[row][col]:
                    island = dfs(row, col)
                    if island:
                        island_count += 1
        return island_count
