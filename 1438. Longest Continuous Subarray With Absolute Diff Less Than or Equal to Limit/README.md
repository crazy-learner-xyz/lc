Given hint:\
Use a sliding window approach keeping the maximum and minimum value using a data structure like a multiset from STL in C++.\
Pre:\
\
总：\
Two pointer. l, r pointer, l,r initialized to be 0, r keep going right, and always record max_len. \
Keep track of the last best maximum and minimum value of the current subarray as we move r to the right is very important.\
\
分：\
When I move the left pointer, how do I know when will the subarray be valid again. How do I know? After I move left array each time, do max(array), and min(array) again?\
\
P.S. I think Leetcode sliding window category is about the same as Leetcode two pointer category.\
\
Post:\
Test cases:\
[8]\
10\
Max_len was initialized to -inf, should have been initialized to 1.\
[1,5,6,7,8,10,6,5,6]\
4\
When I forgot a condition that consists of A or B, I forgot to change the “or” into “and” in not A and not B.\
[4,8,5,1,7,9]\
6\
Had a if () then BlockA else BlockB structure Forgot to update maxval and minval in both BlockA and BlockB\
TLR exceeded\
Can no longer use minval = min(array) every time anymore.\
Given hint: min_dequeue where elements are monotonously increasing and max_dequeue where elements are monotonously decreasing.\
But how do I know the index correspondence between a min_dequeue and a max_dequeue. I see. When you remove an element from the sliding window, you just pop it from the min_dequeue and from the max_dequeue. And dequeue is just a structure that you can insert from both the right and left, I guess I just didn’t dared to think. \
Is binary search absolutely to find the place to insert it? \
