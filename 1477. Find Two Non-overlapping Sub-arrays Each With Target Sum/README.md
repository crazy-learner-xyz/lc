思路(Python)\
Find two non-overlapping subarrays, such that each of these subarray sum of to be equal to the target. Among all such pairs, find the smallest lenA + lenB, such that lenA = len(subarray1) and lenB and len(subarray2). \
\
Brute force solution: Iterate with i, find all the subarrays that are equal to the target there is by writing "sum=0; for i in arr: if sum + i >= target: no, if sum + i  < target, if sum - arr[0]", or more like this "lst=[], for i in arr: if sum(lst)+i <= target: lst.append(i); elif sum(lst) + i > target: lst.pop(0), lst.append(i); if sum(lst) == target: record such lst and the start and end index of the lst". And then ther will be N pairs of i,j,we put all the i-s into i-list, and j-s into j-list, and length into len-list, and for each i, find the shortest length amongst the j-lists that has the shortest list. \
\
The time complexity of this could be very big for certain cases. Are there other ways?\
\
Given hint: Let's create two arrays prefix and suffix where prefix[i] is the minimum length of sub-array ends before i and has sum = k, suffix[i] is the minimum length of sub-array starting at or after i and has sum = k.\
\
Q1. How do i find that prefix[i] and suffix[i]?\
A1. prefix[i+1] = prefix[i], sub-array[i]?
Would there be a subarray that contains i+1, that also sums to be k, that is shorter than prefix[i]? That's the only thing we need to make sure. (CaseA)\
This can be made sure with the method that I mentioned in my brute force solution. \
So at each i, we first make sure whether or not there is case A, and then update prefix[i+1].\
What about suffix?\
suffix[i-1] = suffix[i], subarray[i-1:somewhere]
sum(arr) - sum(array found in prefix) - all numbers popped before.
Once I got prefix[i], and sub-array that contains[i+1], what do I know about sub-array that contains i+2. We don't actually know it, because we haven't been there then.\
Fine, then let's loop from the back of arr to the front as well. The time complexity is just 2 * O(n), is still OK.\
How do I revert "lst=[], for i in arr: if sum(lst)+i <= target: lst.append(i); elif sum(lst) + i > target: lst.pop(0), lst.append(i); if sum(lst) == target: record such lst and the start and end index of the lst"?\
lst = [], starting from i = len(arr)-1 to i = 0: if sum(lst) + i<=target: lst.append(i); elif sum(lst)+i > target:lst.pop(0), lst.append(i); if sum(lst) == target: record such lst. Pretty much the same.\
\
Q2. How do I use prefix[] and suffix[] to get the final result?\
A2. For each i, get prefix[i] + suffix[i]. And then get the minimum of these.\
\
I need to test this "lst=[], for i in arr: if sum(lst)+i < target: lst.append(i); elif sum(lst) + i > target: lst.pop(0), lst.append(i); if sum(lst) == target: record such lst and the start and end index of the lst". Tested fine.\
\
Test cases:\
prefix[i] and suffix[i] shouldn't have overlap.
TLE:\
I guess instead of using sum() and len() functions all the time, I should just keep count for them and then use simple arithmetics.\
No.\
Given hint: Somebody in the Discussion section uses dict as the data structure.\
Java Hashmap?\
Ah, so when they get the sum, they don't add one element by another and delete one element by another like I did, but delete 1:i by 1:?. And 1:? can be determined by finding the value that has the key sum(arr[1:i])-target in the hashmap that stores all the key value pairs where key is the sum(arr[1:?]), and value is ?.\

