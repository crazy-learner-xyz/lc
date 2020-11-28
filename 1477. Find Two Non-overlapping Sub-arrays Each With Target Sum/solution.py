class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        prefix = [len(arr)+1] * len(arr) # initialized to an unreachable number
        lst = []
        for i in range(len(arr)): 
            while lst and sum(lst)+arr[i] > target:
                lst.pop(0)
            lst.append(arr[i])

            if sum(lst) == target:
                if i == 0:
                    prefix[i] = len(lst)
                else:
                    prefix[i] = min(prefix[i-1], len(lst))
            elif i!= 0: #if i=0, then default
                prefix[i] = prefix[i-1]
        prefix = [len(arr)+1] + prefix[:-1]
        
        lst = []
        suffix = [len(arr)+1] * len(arr)
        for i in range(len(arr)-1, 0, -1): 
            while lst and  sum(lst)+arr[i] > target:
                lst.pop(0)
            lst.append(arr[i])

            if sum(lst) == target:
                if i == len(arr)-1:
                    suffix[i] = len(lst)
                else:
                    suffix[i] = min(suffix[i+1], len(lst))
            elif i != len(arr)-1:
                suffix[i] = suffix[i+1]

        print("prefix")
        print(prefix)
        print("suffix")
        print(suffix)
        two_arrays = [prefix[i] + suffix[i] for i in range(len(suffix))]
        if min(two_arrays) > len(arr):
            return -1
        else:
            return min(two_arrays)
