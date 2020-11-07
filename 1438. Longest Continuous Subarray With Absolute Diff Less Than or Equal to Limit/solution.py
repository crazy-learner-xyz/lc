class Solution(object):
    def longestSubarray(self, nums, limit):
    	l, r = 0, 0
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
