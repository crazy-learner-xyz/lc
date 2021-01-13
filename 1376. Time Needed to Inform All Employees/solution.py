class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        subordinate = {}
        for i in range(len(manager)):
            subordinate[manager[i]] = subordinate.get(manager[i],[]) + [i]
        lst = [[headID,0]]
        glob_max = 0
        while lst != []:
            cur_lst = lst.pop(0)
            cur_ID = cur_lst[0]
            cur_time = cur_lst[1]
            next_time = cur_time + informTime[cur_ID]
            glob_max = max(glob_max, next_time)
            if cur_ID in subordinate.keys():
                lst += [[i, next_time] for i in subordinate[cur_ID]]
                
        return glob_max
