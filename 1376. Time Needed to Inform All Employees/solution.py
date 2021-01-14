
class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        subordinate = collections.defaultdict(list)
        for i in range(len(manager)):
            subordinate[manager[i]].append(i)
        lst = [(headID,0)]
        glob_max = 0
        while lst != []:
            cur_ID, cur_time = lst.pop(0)
            next_time = cur_time + informTime[cur_ID]
            glob_max = max(glob_max, next_time)
            for i in subordinate[cur_ID]:
                lst.append((i, next_time))
                
        return glob_max
