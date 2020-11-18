总：\
You want to know the order of these operations, for example, if you had 5 elements in pushed (5 pushes), and 5 elements in popped (5 pops), then you want to know the order of these 10 operations. Also, dictates that len(pushed) != len(popped), hence we want to arrange the order of these 10 operations such that they start at an empty array and end at an empty array.\
Keep pushing elements onto the stack until element is equal to the first element on pop.\
\
Given hint: simulation of stack until the current element being pushed is equal to the first element of the popped array. \
\
Second try:\
总：\
Simulate all the push operations and pop operations until both is empty or until some invalid operations show up. \
\
Thought1:\
Q: How to know what is the right order of push operations and pop operations?\
A:\
1.	Default is push, as long as push is not empty\
2.	If the last element in stack can be found in pop, then the next operation is pop.\
3.	Default is pop, when push is empty. (This is where the invalid operations could appear)\
\
Thought2:\
Q: What other invalid operations could there be? Such as popped keeps popping even when stack is not empty?\
A: No, that never happens. \
