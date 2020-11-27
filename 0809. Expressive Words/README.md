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
\
总：\
I'm trying to get the right logic of if-else conditions. And I test it by just putting that logic on the hello, heeellooo pair, and start from i,j=0,0, until i,j reaches the end, and for each iteration, check if the conditions I made up will make it work like supposed to. \
\
分：\
for W in words, If S[j] == W[i] and S[j+1] != W[i], i+=1, j+=1; If S[j] == W[i] and S[j+1] != W[i], i=1, j+=1. This wouldn't work.\
\
If S[j] == W[i] and S[j+1] != W[i+1] and S[j+2] == S[j+1] == S[j], then move j to the furthest position of k such that S[k] == S[j]. If S[j] == W[i] and S[j+1] != W[i+1] and !(S[j+2] == S[j+1] == S[j]), then fail. If S[j] == W[i] and S[j+1] == W[i+1], then i+=1, j+=1.\
\
But what about the case where W = "heello", and S = "heeellooo"?\
\
Try swapping the order of the S[j+2] == S[j+1] == S[j] condition and the S[j+1] == W[i+1] condition.\
If S[j] == W[i] and S[j+2] ==S[j+1] == S[j], move j to the furthest next position, move i to the furthest next position, make sure that the number of times i moved is not bigger than the number of times j moved (else return False). Else if S[j] == W[i], j+=1, i+=1. Else, return False.\
i,j starts at 0,0 and stops at i<=len(W)-1 and j<=len(S)-1, and this is the while loop stopping condition.\
After the while loop, if i != len(W)-1 or j != len(S)-1, return False. And if this last condition is also passed, return True.\
\
Test cases:\
After test cases, realized the last condition after the while loop should be if i != len(W) or j != len(S), since i,j would have incremented to len(W) and len(S) to not pass the stopping condition of the while loop by the time they reach this last condition.
