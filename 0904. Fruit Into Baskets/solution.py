def FruitIntoBaskets(nums):
	l, r = 0, 1
	current_len = 2
	max_len = 2
	current_types = [nums[l], nums[r]]
	while r <= len(nums):
		if nums[r+1] in current_types:
			r += 1 
			current_len += 1
			max_len = max(max_len, current_len)
		else:
			l = r
			r += 1
			current_len = 2
			current_types = [nums[l], nums[r]]
	return max_len
