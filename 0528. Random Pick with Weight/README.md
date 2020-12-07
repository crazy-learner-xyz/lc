思路(Python)\
\
总：
Brute force solution.\
\
Test cases:\
MLE(Memory Limit Exceeded)\
\
总：\
Used new implementation\
from numpy.random import choice\
draw = choice(list_of_candidates, number_of_items_to_pick,\
              p=probability_distribution)\
\
Test cases:\
TLE\
\
Given hint: Use binary search. \
总：\
How to use binary search on this\
What is g(m)?\
Say we have [1,3], and hence [0,1,1,1]
We generate one number between 0 and len(this list)\
Previously, we did random choice to on the entire list. Now, we do random choice on number.
Once we've chosen the number, we know that between 0 and 1 is 0, and between 1 and 3 is 1.
And so we find the smallest number that is below it\
So we have a list called [1,3,]\
Use binary search to find the first element that is smaller than the sum of everything before it.
\
分：\
Use new implementation\
import bisect\
return bisect.bisect_left(self.new_w,r)\
