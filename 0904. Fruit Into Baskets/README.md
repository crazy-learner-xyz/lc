思路：
总：
Find longest subarray with only two types

Two pointer
l and r are equal to 0 and 1, respectively. While r hasn't reached len(nums), we judge whether or not the element at index r+1 is equal to one of the two current types. If yes, then r += 1, current array len += 1. If no, then r move to the right, l move to where r previously was, and then current array len = 2.

