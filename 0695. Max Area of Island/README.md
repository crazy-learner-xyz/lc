1. Brute force pseudocode

neighborhood = {}
land = {}
for i in rows:
	for j in cols:
		for neighbor in {the four neighbors of grid[i][j]}
			check if the neighbor is in neighborhood
			if yes:
				for neighbor1 in neighborhood[neighbor]:
					land += 1
					recurse

2. DFS pseudocode
def checkGrid(m, n, stack, grid, s):
	if grid[m][n] == 1:
		stack.append((m, n, s+1))
		grid[m][n] = -1
	else:
		grid[m][n] = -1


def SearchAllLand(m, n, grid):
	#DFS
	stack = []
	while stack:
		m, n, s = stack.pop(-1)
		max_area = max(max_area, s)
		checkGrid(m+1, n, stack, grid, s)
		checkGrid(m-1, n, stack, grid, s)
		checkGrid(m, n+1, stack, grid, s)
		checkGrid(m, n-1, stack, grid, s)


max_area = 0

def maxAreaOfIsland():
	for i in rows:
		for j in cols:
			if grid[i][j] != 0:
				SearchAllLand(grid[i][j])
			grid[i][j] == -1


3. DFS code
class Solution(object):

    def checkGrid(self,m, n, stack, grid, s):
        if not (m > len(grid)-1 or n > len(grid[0])-1 or m < 0 or n < 0):
            if grid[m][n] == 1:
                stack.append((m, n, s+1))
            grid[m][n] = 2


    def SearchAllLand(self,m, n, grid):
        #DFS
        stack = [(m, n, 1)]
        while stack:
            print(stack)
            m, n, s = stack.pop(-1)
            self.max_area = max(self.max_area, s)
            self.checkGrid(m+1, n, stack, grid, s)
            self.checkGrid(m-1, n, stack, grid, s)
            self.checkGrid(m, n+1, stack, grid, s)
            self.checkGrid(m, n-1, stack, grid, s)



    def maxAreaOfIsland(self, grid):
        self.max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(grid)
                if grid[i][j] == 1:
                    grid[i][j] = 2   
                    self.SearchAllLand(i, j, grid)
                else:
                    grid[i][j] = 2   
        return self.max_area

4. DFS iterative code after reading Discussion
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