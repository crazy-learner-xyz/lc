思路：\
总：\
Reshape the problem into:\
Find the longest subarray with only two types\
\
Make it easier, what if I want to find the longest subarray with one type?\
We just iterate through it and record the max.\
\
def longestSubarray(nums):\
	max_len = 0\
	current_array_len = 0\
	current_array_elem = INF_MIN\
	for i in range(len(nums)):\
		if nums[i] == current_array_elem:\
			current_array_len += 1\
			if current_array_len > max_len:\
				max_len = current_array_len\
		else:\
			current_array_elem = nums[i]\
			current_array_len = 0\
	return max_len \
However, the longest subarray with only two types cannot use the same iteration like longest subarray with one type, since nums[i] can be either current_type[0] or current_type[1].\
\
总：\
Two Pointer\
l and r are equal to 0 and 1, respectively. While r hasn't reached len(nums), we judge whether or not the element at index r+1 is equal to one of the two current types. If yes, then r += 1, current array len += 1. If no, then r move to the right, l move to where r previously was, and then current array len = 2.\
\
Write algorithm\
\
Debugging the algorithm\
Test cases that failed:\
[0,0,1,1]\
Cause: Current type initiation was from the first two elements of nums. But when the first two elements of nums are of the same type, then the current type really only contains one type.\
Test cases that failed:\
[0,1,6,6,4,4,6]\
Cause: when tree[r+1] is not in current_types, r was set to be equal to l. But when the subarray is [1,6,6], and then there was another 4, l should be set to the first 6, rather than the second 6. Keep track of the first element of the first type in current type, and keep track of the first element of the second type in current type. \
[3,3,3,1,2,1,1,2,3,3,4]\
Cause: The last derivation was wrong. We need to keep tracking of the first continuous element, i.e., the element where it last was. The first element and the tree[r] should form a longestSubarray with only one type.\
