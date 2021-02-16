import collections
class Solution(object):
    
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # Reshape the data structure
        diction = collections.defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected[0])): 
                if isConnected[i][j] == 1:
                    diction[i] += [j]
                    diction[j] += [i]
    
        traversed_lst = []
        numIsland = 0
        for i in range(len(isConnected)):
            if i not in traversed_lst:
                stack = [(i)]
                while stack!= []:
                    i = stack.pop(-1)
                    for j in diction[i]:
                        if j not in traversed_lst: 
                            stack.append((j))
                            traversed_lst.append(j)
                numIsland += 1
        
        return numIsland