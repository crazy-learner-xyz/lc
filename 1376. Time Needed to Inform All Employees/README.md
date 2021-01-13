思路(Python)\
The easiest way is just to traverse the tree. If we traverse each node only once, then it should be alright for 1 <= n <= 10^5 requirement. So how do we construct this tree? \
Establish a dictionary of key (manager ID), value (list of IDs of whoever is underneath him), and keep track of the headID. When we traverse this tree, we start with key = headID, get to values, and then go to each value, and then go to headID, and then get to values. \
Since algorithm part is not that hard, I'll add level of difficulty of implementation, and implement in C++.\
So dictionary is changed to std::map.\
"#include<map>" "std::map<int, int>mapp = {};"\
mapp.insert ( std::pair<int,int>(manager[i],{i}) );\
Remember that the use of curly brackets around a variable in C++ is just initialization. It could be an initialization of an array, i.e, int a[5]={1,2} or an initialization of a struct, i.e., Bar b = {10}, where struct Bar {int i};\
map<int,int>::iterator it = m.find('2');\
int b3;\
if(it != m.end())\
{\
   b3 = it->second;\
}\
Gave up on using C++ to do this. I need more foundation practice with C++. And for leetcode, I would like to keep to Python, because I like Python, and I need exercises in Python too to make sure I maintain good mastery of Python.\
\

\
Testcase that didn't pass:\
15\
0\
[-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]\
[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]\
\
I see, so if id=0 has two subordinates id=1 and id=2, then id=1 will go tell its subordinates cocurrently as id=2 go tell its subordinates, and eventually we take whatever time is bigger in id=1 and id=2.\ 
\
So I think we should do a DFS on this. But how do we inform the parent node of its value, since the parent node would have been deleted when we've explored the child node?  \
\
Refered to this hint:\
使用level order思想，每一次将manager-employee这条权重带入下一个层级运算，然后每一次都更新一个较大的值赋予globalMax，代表了从root到这一个Leaf的权重和。最后返回globalMax的值。\
\
Somehow, there is still TLE. \
