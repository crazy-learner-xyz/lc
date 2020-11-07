class Solution(object):
    def longestSubarray(self, nums, limit):
    	l, r = 0, 0
    	maxval = nums[0]
    	minval = nums[0]
    	max_len = INF_MIN
    	while r <= len(nums)-1:
    		if abs(nums[r+1] - maxval) > limit or abs(nums[r+1] - minval) > limit:
    			r += 1
    			while true:
    				l+=1
    				maxval = max(nums[l:r+1])
    				minval = min(nums[l:r+1])
    				if abs(nums[r+1] - maxval) <= limit or abs(nums[r+1] - minval) <= limit:
    					break
    			max_len = r - l + 1
    		else:
    			r += 1
    			max_len = max(max_len, r-l+1)
    	return max_len

