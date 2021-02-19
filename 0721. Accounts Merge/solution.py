
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        #Search for ones that have the same names, amongst the ones that have the same names, 
        #Read the hints. But what is the data structure for this kind of graph?
        diction = {}
        for account in accounts:
            if account[0] in diction.keys():
                graph = diction[account[0]] 
                found = False
                i = 0
                while not found and i < len(account):
                    j = 0
                    while not found and j < len(graph):
                        if account[i] in graph[j]:
                            graph[j] += set(account)
                            found = True
            else:
                diction[account[0]] = [set(account[1:])]
        
        out = []
        for i in diction.keys():
            out.append([i] + list(diction[i]))
            
        return out