思路(Python)\
总：\
If S has a substring that contains only 2 of the same element, then that's impossible to reach unless the start string already has the substring that contains 2 of the same element.\
If S has a substring that contains only 1 of the same element, then that's impossible to reach unless the start string already has the substring that contains 1 of the same element.\
Also, the order of each continuous subsequence must be the same. The start string must already have the single element version of all the elements in S, and then in the correct order.\
分：\
Step 1. Iterate through S and get list A of all the elements in S, in correct order, and get list B of all the frequency of each element in A.\
Step 2. For each word, iterate through word, and and the end of each continuous substring of the same element. If a continuous substring cannot me made into the substring like in S, then break right there.\
\
In S\
If s is equal to cur_char, then cur_freq += 1, if s is not equal to cur_char, then add cur_char, cur_freq to char_list, freq_list, reset cur_char, cur_freq to the new char, 1. Until i = len(S)-1\
\
In word\
pop the first cur_char and cur_freq from char_list, freq_list. if s is equal to the first cur_char, then continue, else return. add the word_freq. When s is no longer equal to the first cur_char, check the size of the word_freq, see if it is equal to the cur_freq. If not, see if cur_freq == 3, if not, return. \
\
Testcase: \
"heeellooo"\
["hello", "hi", "helo"]\
If s is equal to the cur_char, there are two cases. One, if the s_freq is equal to the cur_freq, that means all chars of s is at its end, hence j+=1. Two, if the s_Freq is not equal to the cur_freq, that means there are still more chars of s, hence i+=1. \
\
Also, the previous algorithm disregarded the case when there are double "l" in word, When there is double "l" in S and double "l" in word, what to do?\
\
Is there a better way than writing out all the cases?\
\
Given hint: Some people didn't sum up S first and then do word, but instead used two-pointers and a check function from the start.\
