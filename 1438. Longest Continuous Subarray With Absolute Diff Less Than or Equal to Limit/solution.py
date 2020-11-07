from collections import deque  

class Solution(object):
    def binaryInsertMinQueue(deq, number):
        #find the largest element that is smaller than number
        l, r = 0, len(deq)+1
        while l < r:
            m = (l+r) // 2
            if deq[m] >= number:
                r = m
            else:
                l = m+1
        return l-1
    
    def binaryInsertMaxQueue(deq, number):
        #find the smallest element that is larger than number
        l, r = 0, len(deq)+1
        while l < r:
            m = (l+r) // 2
            if deq[m] <= number:
                r = m
            else:
                l = m+1
        return l-1
    
    
    def longestSubarray(self, nums, limit):
    	l, r = 0, 0
        minqueue = deque(nums[0])
        maxqueue = deque(nums[0])
    	maxval = nums[0]
    	minval = nums[0]
    	max_len = 1
    	while r <= len(nums)-2:
            if abs(nums[r+1] - maxval) > limit or abs(nums[r+1] - minval) > limit:
                r += 1
                maxval = max(nums[l:r+1])
                minval = min(nums[l:r+1])
                while abs(nums[r] - maxval) > limit or abs(nums[r] - minval) > limit:
                    l+=1
                    maxval = max(nums[l:r+1])
                    minval = min(nums[l:r+1])
            else:
                r += 1
                #print(l,r)
                max_len = max(max_len, r-l+1)
                maxval = max(maxval, nums[r])
                minval = min(minval, nums[r])
    	return max_len
