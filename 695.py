class Solution(object):
    def maxAreaOfIsland(self, grid):

        if len(grid) == 0:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        final = []
        

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1

            area += dfs(r, c-1)
            area += dfs(r+1, c)
            area += dfs(r, c+1)
            area+= dfs(r-1, c)

            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    final.append(dfs(i, j))
        return max(final) if final else 0



        """
        :type grid: List[List[int]]
        :rtype: int
        """
        