思路(Python)\
总：\
You want to know the order of these operations, for example, if you had 5 elements in pushed (5 pushes), and 5 elements in popped (5 pops), then you want to know the order of these 10 operations. Also, dictates that len(pushed) != len(popped), hence we want to arrange the order of these 10 operations such that they start at an empty array and end at an empty array.\
Keep pushing elements onto the stack until element is equal to the first element on pop.\
\
Given hint: simulation of stack until the current element being pushed is equal to the first element of the popped array. \
\
总：\
O(n) complexity\
\
What about pop 2 elements at the same time?\
