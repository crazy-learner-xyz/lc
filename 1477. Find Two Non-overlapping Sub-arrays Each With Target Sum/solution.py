class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        diction = {}
        diction2 = {}
        s = 0
        s_arr = sum(arr)
        for i in range(len(arr)):
            s += arr[i]
            diction[s] = i
            diction2[s] = s_arr - s
        
        
        prefix = [float('inf')] * len(arr) # initialized to an unreachable number
        lst = []
        s_lst = 0
        for i in range(len(arr)): 
            s_lst += arr[i]
            if s_lst == target:
                if i == 0:
                    prefix[i] = 1
                else:
                    prefix[i] = min(prefix[i-1], i-0+1)
            elif s_lst + target in diction2.keys():
                prefix[i] = min(prefix[i-1], diction2[s_lst + target]-i)            
            elif i!= 0: #if i=0, then default
                prefix[i] = prefix[i-1]
        prefix = [float('inf')] + prefix[:-1]
        
        suffix = [float('inf')] * len(arr)
        lst = []
        s_lst = 0
        for i in range(len(arr)-1, 0, -1): 
            s_lst += arr[i]
            if s_lst == target:
                if i == len(arr)-1:
                    suffix[i] = 1
                else:
                    suffix[i] = min(suffix[i+1], i-0+1)
            elif s_lst - target in diction.keys():
                if i == len(arr)-1:
                    suffix[i] =  i-diction[s_lst - target]+1
                else:
                    suffix[i] = min(suffix[i+1], i-diction[s_lst - target]+1)            
            elif i!= len(arr)-1: #if i=0, then default
                suffix[i] = suffix[i+1]

        two_arrays = [prefix[i] + suffix[i] for i in range(len(suffix))]
        if min(two_arrays) > len(arr):
            return -1
        else:
            return min(two_arrays)
