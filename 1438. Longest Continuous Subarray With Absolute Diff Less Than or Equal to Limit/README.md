Given hint:\
Use a sliding window approach keeping the maximum and minimum value using a data structure like a multiset from STL in C++.\
\
总：\
Two pointer. l, r pointer, l,r initialized to be 0, r keep going right, and always record max_len. \
Keep track of the last best maximum and minimum value of the current subarray as we move r to the right is very important.\
\
分：\
When I move the left pointer, how do I know when will the subarray be valid again. How do I know? After I move left array each time, do max(array), and min(array) again?\
\
P.S. I think Leetcode sliding window category is about the same as Leetcode two pointer category.\

