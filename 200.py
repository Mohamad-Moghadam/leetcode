class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        counts = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
        
            grid[r][c] = "0"
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    counts += 1

        return counts


        """
        :type grid: List[List[str]]
        :rtype: int
        """
        