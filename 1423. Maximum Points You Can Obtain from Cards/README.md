思路(Python)\
总：\
You have k chances to take from either the beginning or the end, and you want the sum of their values to be the greatest. \
Given Hint: DP\
Given one array = [a, subarray, b]\
Best_sum_at_beginning_or_end(array) = Best_sum_at_beginning_or_end(subarray) + max(a, b)\
Best_sum_at_beginning_or_end(array) = Best_sum_at_beginning_or_end(array[1:-1]) + max(array[0], array[-1])\
No. Checked with example.\
Best_sum_at_beginning_or_end(array) = Best_sum_at_beginning_or_end(array[2:-2]) + max(array[0]+array[-2], array[1]+array[-1])\
I cannot find any good DP induction rules.\
Given hint: Let the sum of all points be total_pts. You need to remove a sub-array from cardPoints with length n - k.\
Question: Is this true for any subarray of length n-k that is removed from the array, there is a way to take from either the beginning or the end for k times that reduces the array to that subarray?\
Answer: Yes.\
Problem is reformatted into:\
Find the subarray of length n-k in array that has the smallest sum.\
