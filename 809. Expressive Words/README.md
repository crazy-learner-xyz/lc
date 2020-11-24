思路(Python)\
总：\
If S has a substring that contains only 2 of the same element, then that's impossible to reach unless the start string already has the substring that contains 2 of the same element.\
If S has a substring that contains only 1 of the same element, then that's impossible to reach unless the start string already has the substring that contains 1 of the same element.\
Also, the order of each continuous subsequence must be the same. The start string must already have the single element version of all the elements in S, and then in the correct order.\
分：\
Step 1. Iterate through S and get list A of all the elements in S, in correct order, and get list B of all the frequency of each element in A.
Step 2. For each word, iterate through word, and and the end of each continuous substring of the same element. If a continuous substring cannot me made into the substring like in S, then break right there.