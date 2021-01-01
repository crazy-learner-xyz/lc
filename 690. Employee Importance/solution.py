"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        subordinate = {}
        value = {}
        for em in employees:
            subordinate[em.id] = em.subordinates
            value[em.id] = em.importance
            
        lst = [id]
        importance = 0
        while lst != []:
            cur_id = lst.pop(0)
            importance += value[cur_id]
            if subordinate[cur_id] != []:
                lst += subordinate[cur_id]

        return importance