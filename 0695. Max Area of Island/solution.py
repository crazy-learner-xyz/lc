class Solution(object):

    def checkGrid(self,m, n, stack, grid):
        if not (m > len(grid)-1 or n > len(grid[0])-1 or m < 0 or n < 0):
            if grid[m][n] == 1:
                stack.append((m, n))


    def SearchNewLand(self,m, n, grid):
        #DFS
        s = 0
        stack = [(m, n)]
        #I should be that whenever stack pop it, I make it into 2, not whenever SearchAllLand, I make it into 2, or whenever checkGrid, I make it into 2, or these two combined.
        while stack:
            #print(stack)
            m, n = stack.pop(-1)
            if grid[m][n]:
                grid[m][n] = 0
                s += 1

            self.checkGrid(m+1, n, stack, grid)
            self.checkGrid(m-1, n, stack, grid)
            self.checkGrid(m, n+1, stack, grid)
            self.checkGrid(m, n-1, stack, grid)
        #Also, whenever SearchNewLand, all the areas gains add to each other, so they should all share one s.
        return s


    def maxAreaOfIsland(self, grid):
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print(grid)
                if grid[i][j] == 1:
                    s = self.SearchNewLand(i, j, grid)
                    max_area = max(max_area, s)
        return max_area