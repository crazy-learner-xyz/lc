思路(Python)\
My first thought is sort the hand array, and then iterate through the loop. Start from i=0, test if the next W elements are consecutive. After the W elements, start from the new i, and then test if the next W elements are consecutive. The time complexity is O(n), the memory complexity is O(n).\
But it wouldn't work for the case [1,2,3],[2,3,4],[6,7,8].\
I think we gotta put each head in a dictionary, and then fill into these dictionaries. And in the end, we check if these dictionaries are filled. \
[1,2,3,6,2,3,4,7,8]\
[1,2,2,3,3,4,6,7,8]\
[1,2,3]
[2,3]
Sort it first. Then iterate through hand. If it can be filled into existing lists, fill it into existing lists, if it cannot, then create a new list.\
How do we check whether or not it's in this list, fast?\
Keep a list of the index they lack? \
No, append 3:[], and then delete 2:[]\
The data structure need some thought.\
[1]:2, [1,2]:3, [1,2]:3,[2]:3, [1,2,3]:4,[2,3]:4, \
[[1]],[2], [[1,2]],[3], [[1,2],[2]],[3,3], [[1,2,3],[2,3]],[4,4], \
If it's this way, then the time complexity will be O(n^2).\
Still get a dictionary instead.\
{2:[1]}, {3:[1,2]}, {3:[1,2],3:[2]}, {4:[1,2,3] /then deleted, so wouldn't have it, /,4:[2,3]}, {4:[2,3]}\
The memory complexity of the dictionary is about the same as the memory complexity of two lists.\
What about duplicate keys?\
{2:[[1]]}, {3:[[1,2]]}, {3:[[1,2],[2]]}, {4:[1,2,3] /then deleted, so wouldn't have it, /,4:[2,3]}, {4:[2,3]}\
{4:[2,3,4]/deleted/}, {}, {7:[6]}, {8:[6,7]},{8:[6,7,8]/deleted/}, {}\

\

Additional thoughts: test case: what if W = 1?\
\
Submission 1. Passed 3 test cases. The first test case that didn't pass is:
[1,2,3]\
1\
\
Ah I knew it, there's the problem with W = 1. \
No need to integrate W = 1 into the core algorithm, if W = 1, just directly return true. \
\
Submission 2. Passed 13 test cases. The first test case that didn't pass is:\
[9,13,15,23,22,25,4,4,29,15,8,23,12,19,24,17,18,11,22,24,17,17,10,23,21,18,14,18,7,6,3,6,19,11,16,11,12,13,8,26,17,20,13,19,22,21,27,9,20,15,20,27,8,13,25,23,22,15,9,14,20,10,6,5,14,12,7,16,21,18,21,24,23,10,21,16,18,16,18,5,20,19,20,10,14,26,2,9,19,12,28,17,5,7,25,22,16,17,21,11]
10\
\
Is there a duplicate case that I didn't see? After writing the values of each iteration down on paper, turns out there was a little implementation bug, I wrote hand[i+1] where it should have been hand[i]+1.\
\
Submission 3. Accepted. Runtime: 4848 ms, faster than 5.24% of Python online submissions for Hand of Straights.\
Memory Usage: 18 MB, less than 6.37% of Python online submissions for Hand of Straights.\


